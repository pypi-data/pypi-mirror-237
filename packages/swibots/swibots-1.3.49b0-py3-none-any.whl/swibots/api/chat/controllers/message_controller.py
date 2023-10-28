import asyncio
import os
import json
from inspect import iscoroutinefunction
import logging
from typing import TYPE_CHECKING, List, Optional
from asyncio.tasks import Task
from swibots.error import CancelError
from swibots.api.chat.models import (
    Message,
    GroupChatHistory,
    InlineMarkup,
    InlineQuery,
    InlineQueryAnswer,
)
from swibots.api.common.models import User, MediaUploadRequest, Media, EmbeddedMedia
from swibots.api.community.models import Channel, Group

if TYPE_CHECKING:
    from swibots.api.chat import ChatClient

log = logging.getLogger(__name__)

BASE_PATH = "/v1/message"


class MessageController:
    """Message controller

    This controller is used to communicate with the message endpoints.

    """

    def __init__(self, client: "ChatClient"):
        self.client = client

    async def new_message(
        self,
        to: Optional[int | User] = None,
        channel: Optional[Channel | str] = None,
        group: Optional[Group | str] = None,
    ) -> Message:
        """Create a new message"""
        if isinstance(to, User):
            to = to.id

        if isinstance(channel, Channel):
            channel = channel.id

        if isinstance(group, Group):
            group = group.id

        return Message(
            user_id=self.client.user.id,
            receiver_id=to,
            channel_id=channel,
            group_id=group,
            app=self.client.app,
        )

    async def get_messages(self, user_id: int = None) -> List[Message]:
        """Get messages for a user

        Parameters:
            user_id (``int``, *optional*): The user id. Defaults to the current user id.

        Returns:
            ``List[~switch.api.chat.models.Message]``: The messages

        Raises:
            ``~switch.error.SwitchError``: If the messages could not be retrieved
        """
        if user_id is None:
            user_id = self.client.user.id
        log.debug("Getting messages for user %s", user_id)
        response = await self.client.get(f"{BASE_PATH}/{user_id}")
        return self.client.build_list(Message, response.data)

    async def _send_file(self, url, form_data, media: MediaUploadRequest):
        upload_req, files = media.file_to_request(url)
        response = await self.client.post(url, form_data=form_data, files=files)
        files["uploadMediaRequest.file"][1].close()
        return response

    async def send_message(
        self, message: Message, media: MediaUploadRequest | EmbeddedMedia = None
    ) -> Message | Task:
        """Send a message

        Parameters:
            message (``~switch.api.chat.models.Message``): The message to send
            media (``~switch.api.common.models.MediaUploadRequest``, *optional*): The media to send with the message

        Returns:
            ``~switch.api.chat.models.Message``: The message

        Raises:
            ``~switch.error.SwitchError``: If the message could not be sent
        """
        async def __process():
            _embedded = isinstance(media, EmbeddedMedia)
            if _embedded:
                message.status = 4
            data = message.to_json_request()
            log.debug("Sending message %s", json.dumps(data))

            if isinstance(media, MediaUploadRequest):
                data["mediaInfo"] = await media.get_media()

            if _embedded:
                data["embedMessage"] = media.to_json_request()
            response = await self.client.post(f"{BASE_PATH}/create", data=data)
            return self.client.build_object(Message, response.data["message"])
        task = asyncio.get_event_loop().create_task(__process())
        if media and not media.block:
            return task
        return await task

    async def send_text(
        self,
        text: str,
        to: Optional[int | User] = None,
        channel: Optional[Channel | str] = None,
        group: Optional[Group | str] = None,
        inline_markup: InlineMarkup = None,
        media: MediaUploadRequest = None,
    ) -> Message:
        """Send a message with text

        Parameters:
            to (``int`` | ``~switch.api.common.models.User``, *optional*): The user id to send the message to. Defaults to the current user id.
            text (``str``): The text to send
            channel (``~switch.api.community.models.Channel``, *optional*): The channel to send the message to
            group (``~switch.api.community.models.Group``, *optional*): The group to send the message to
            inline_markup (``~switch.api.chat.models.InlineMarkup``, *optional*): The inline markup to send with the message
            media (``~switch.api.common.models.MediaUploadRequest``, *optional*): The media to send with the message

        Returns:
            ``~switch.api.chat.models.Message``: The message

        Raises:
            ``~switch.error.SwitchError``: If the message could not be sent
        """
        message = await self.new_message(to, channel, group)
        message.message = text
        message.inline_markup = inline_markup
        return await self.send_message(message, media)

    async def reply(
        self,
        message: int | Message,
        reply: Message,
        media: MediaUploadRequest | EmbeddedMedia = None,
    ) -> Message:
        if isinstance(message, Message):
            id = message.id
        else:
            id = message
        reply.replied_to_id = id
        return await self.send_message(reply, media)

    async def reply_text(
        self,
        message: int | Message,
        text: str,
        inline_markup: InlineMarkup = None,
        media: MediaUploadRequest | EmbeddedMedia = None,
        cached_media: Media = None,
    ) -> Message:
        """Reply to a message with text

        Parameters:
            message (``~switch.api.chat.models.Message``): The message to reply to
            text (``str``): The text to reply with

        Returns:
            ``~switch.api.chat.models.Message``: The message

        Raises:
            ``~switch.error.SwitchError``: If the message could not be sent
        """
        m = message._prepare_response()
        if text:
            m.message = text
        m.inline_markup = inline_markup
        m.cached_media = cached_media

        if isinstance(message, Message):
            id = message.id
        else:
            id = message

        return await self.reply(id, m, media)

    async def edit_message(
        self, message: Message, media: EmbeddedMedia | MediaUploadRequest = None
    ) -> Message:
        """Edit a message

        Parameters:
            message (``~switch.api.chat.models.Message``): The message to edit

        Returns:
            ``~switch.api.chat.models.Message``: The message

        Raises:
            ``~switch.error.SwitchError``: If the message could not be edited
        """
        embedded = isinstance(media, EmbeddedMedia)
        new_message = Message(
            self.client.app,
            message=message.message,
            inline_markup=message.inline_markup,
            embed_message=message.embed_message,
            id=message.id,
        )

        if embedded:
            if isinstance(media.thumbnail, MediaUploadRequest):
                response_media = await self.client.app.upload_media(media.thumbnail)
                media.thumbnail = response_media.url
            new_message.embed_message = media

        data = new_message.to_json_request()
        log.debug("Editing message %s", json.dumps(data))

        response = await self.client.put(f"{BASE_PATH}?id={message.id}", data=data)

        return self.client.build_object(Message, response.data["message"])

    async def edit_message_text(
        self,
        message: int | Message,
        text: str,
        media: EmbeddedMedia = None,
        inline_markup: InlineMarkup = None,
    ) -> Message:
        """Edit a message with text

        Parameters:
            message (``~switch.api.chat.models.Message``): The message to edit
            text (``str``): The text to edit with

        Returns:
            ``~switch.api.chat.models.Message``: The message

        Raises:
            ``~switch.error.SwitchError``: If the message could not be edited
        """
        if isinstance(message, Message):
            id = message.id
        else:
            id = message

        return await self.edit_message(
            Message(id=id, message=text, inline_markup=inline_markup), media
        )

    async def delete_message(self, message: int | Message) -> bool:
        """Delete a message

        Parameters:
            message (``int`` | ``~switch.api.chat.models.Message``): The message id or message to delete

        Returns:
            ``bool``: True if the message was deleted

        Raises:
            ``~switch.error.SwitchError``: If the message could not be deleted
        """
        if isinstance(message, Message):
            id = message.id
        else:
            id = message
        log.debug("Deleting message %s", id)
        response = await self.client.delete(f"{BASE_PATH}/{id}")
        return True

    async def delete_messages_from_user(
        self, recipient_id: int, user_id: int = None
    ) -> bool:
        """Delete messages from a user

        Parameters:
            recipient_id (``int``): The recipient id
            user_id (``int``, *optional*): The user id. Defaults to the current user id.

        Returns:
            ``bool``: True if the messages were deleted

        Raises:
            ``~switch.error.SwitchError``: If the messages could not be deleted

        """
        log.debug("Deleting messages for user %s", recipient_id)
        if user_id is None:
            user_id = self.client.user.id

        response = await self.client.delete(f"{BASE_PATH}/{user_id}/{recipient_id}")
        return True

    async def get_messages_between_users(
        self,
        recipient_id: int,
        user_id: int = None,
        page_limit: int = 100,
        page_offset: int = 0,
    ) -> List[Message]:
        """Get messages between two users

        Parameters:
            recipient_id (``int``): The recipient id
            user_id (``int``, *optional*): The user id. Defaults to the current user id.
            page_limit (``int``, *optional*): The page limit. Defaults to 100.
            page_offset (``int``, *optional*): The page offset. Defaults to 0.

        Returns:
            ``List[~switch.api.chat.models.Message]``: The messages

        Raises:
            ``~switch.error.SwitchError``: If the messages could not be retrieved
        """
        q = []
        if page_limit:
            q.append(f"pageLimit={page_limit}")
        if page_offset:
            q.append(f"pageOffset={page_offset}")

        str_q = "&".join(q)

        if user_id is None:
            user_id = self.client.user.id

        log.debug("Getting messages for user %s", recipient_id)
        response = await self.client.get(
            f"{BASE_PATH}/{user_id}/{recipient_id}?{str_q}"
        )
        return self.client.build_list(Message, response.data["messages"])

    async def forward_message(
        self,
        message: Message | int,
        group_channel: Optional[Group | Channel | str] = None,
        receiver_id: Optional[str] = None,
    ) -> Message:
        """Forward a message to a group or user

        Parameters:
            message (``~switch.api.chat.models.Message`` | ``int``): The message to forward
            group_channel (``~switch.api.chat.models.Group`` | ``~switch.api.chat.models.Channel`` | ``str``, *optional*): The group or channel to forward to. Defaults to None.
            receiver_id (``str``, *optional*): The user id to forward to. Defaults to None.

        Returns:
            ``~switch.api.chat.models.Message``: The message

        Raises:
            ``~switch.error.SwitchError``: If the message could not be forwarded
        """
        if isinstance(message, Message):
            id = message.id
        else:
            id = message

        if isinstance(group_channel, (Group, Channel)):
            group_channel = group_channel.id
        elif group_channel is not None:
            group_channel = group_channel

        q = []
        if group_channel is not None:
            q.append(f"groupChannelId={group_channel}")
        if receiver_id is not None:
            q.append(f"receiverId={receiver_id}")

        strQuery = "&".join(q)

        log.debug("Forwarding message %s", id)
        response = await self.client.put(f"{BASE_PATH}/forward/{id}?{strQuery}")
        return self.client.build_object(Message, response.data["message"])

    async def get_message(self, message_id: int) -> Message:
        """Get a message by id

        Parameters:
            message_id (``int``): The message id, if a Message is passed, the id will be extracted from it.

        Returns:
            ``~switch.api.chat.models.Message``: The message

        Raises:
            ``~switch.error.SwitchError``: If the message could not be retrieved
        """
        if isinstance(message_id, Message):
            id = message_id.id
        else:
            id = message_id
        log.debug("Getting message %s", id)
        response = await self.client.get(f"{BASE_PATH}/findOne/{id}")
        return self.client.build_object(Message, response.data)

    async def get_group_chat_history(
        self,
        group_id: str,
        community_id: str,
        user_id: int = None,
        page_limit: int = 100,
        page_offset=0,
    ) -> GroupChatHistory:
        """Get group chat history

        Parameters:
            group_id (``str``): The group id
            community_id (``str``): The community id
            user_id (``int``, *optional*): The user id. Defaults to the current user id.
            page_limit (``int``, *optional*): The page limit. Defaults to 100.
            page_offset (``int``, *optional*): The page offset. Defaults to 0.

        Returns:
            ``~switch.api.chat.models.GroupChatHistory``: The group chat history

        Raises:
            ``~switch.error.SwitchError``: If the group chat history could not be retrieved

        """
        log.debug("Getting group chat history for group %s", group_id)
        q = ["isChannel=false"]
        if page_limit:
            q.append(f"pageLimit={page_limit}")
        else:
            q.append(f"pageLimit=0")
        if page_offset:
            q.append(f"pageOffset={page_offset}")
        else:
            q.append(f"pageOffset=0")
        if community_id:
            q.append(f"communityId={community_id}")

        str_q = "&".join(q)

        if user_id is None:
            user_id = self.client.user.id

        response = await self.client.get(
            f"{BASE_PATH}/group/{user_id}/{group_id}?{str_q}"
        )
        return self.client.build_object(GroupChatHistory, response.data)
        # return GroupChatHistory.build_from_json(response.data)

    async def get_channel_chat_history(
        self,
        channel_id: str,
        community_id: str,
        user_id: int = None,
        page_limit: int = 100,
        page_offset=0,
    ) -> GroupChatHistory:
        """Get channel chat history

        Parameters:
            channel_id (``str``): The channel id
            community_id (``str``): The community id
            user_id (``int``, *optional*): The user id. Defaults to the current user id.
            page_limit (``int``, *optional*): The page limit. Defaults to 100.
            page_offset (``int``, *optional*): The page offset. Defaults to 0.

        Returns:
            ``~switch.api.chat.models.ChannelChatHistory``: The channel chat history

        Raises:
            ``~switch.error.SwitchError``: If the channel chat history could not be retrieved

        """
        log.debug("Getting channel chat history for channel %s", channel_id)
        q = ["isChannel=true"]
        if page_limit:
            q.append(f"pageLimit={page_limit}")
        else:
            q.append(f"pageLimit=0")
        if page_offset:
            q.append(f"pageOffset={page_offset}")
        else:
            q.append(f"pageOffset=0")
        if community_id:
            q.append(f"communityId={community_id}")

        str_q = "&".join(q)

        if user_id is None:
            user_id = self.client.user.id

        response = await self.client.get(
            f"{BASE_PATH}/group/{user_id}/{channel_id}?{str_q}"
        )
        return self.client.build_object(GroupChatHistory, response.data)
        # return GroupChatHistory.build_from_json(response.data)

    async def get_community_media_files(self, community_id: str) -> List[Message]:
        """Get community media files

        Parameters:
            community_id (``str``): The community id

        Returns:
            ``List[~switch.api.chat.models.Message]``: The community media files

        Raises:
            ``~switch.error.SwitchError``: If the community media files could not be retrieved
        """
        log.debug("Getting community media files for community %s", community_id)
        response = await self.client.get(
            f"{BASE_PATH}/media?communityId={community_id}"
        )
        return self.client.build_list(Message, response.data)
        # return Message.build_from_json_list(response.data)

    async def get_community_media_files_by_status(
        self, community_id: str, status: str
    ) -> List[Message]:
        """Get community media files by status

        Parameters:
            community_id (``str``): The community id
            status (``str``): The status of the media files

        Returns:
            ``List[~switch.api.chat.models.Message]``: The community media files


        Raises:
            ``~switch.error.SwitchError``: If the community media files could not be retrieved
        """
        log.debug("Getting community media files for community %s", community_id)
        response = await self.client.get(
            f"{BASE_PATH}/media?communityId={community_id}&status={status}"
        )
        return self.client.build_list(Message, response.data)
        # return Message.build_from_json_list(response.data)

    async def get_user_media_files(self, user_id: int = None) -> List[Message]:
        """Get user media files


        Parameters:
            user_id (``int``, *optional*): The user id. Defaults to the current user id.

        Returns:
            ``List[~switch.api.chat.models.Message]``: The user media files

        Raises:
            ``~switch.error.SwitchError``: If the user media files could not be retrieved
        """
        if user_id is None:
            user_id = self.client.user.id
        log.debug("Getting user media files for user %s", user_id)
        response = await self.client.get(f"{BASE_PATH}/media/{user_id}")
        return self.client.build_list(Message, response.data)
        # return Message.build_from_json_list(response.data)

    async def clear_conversation(self, receiver_id: int) -> bool:
        """Clear a conversation

        Parameters:
            receiver_id (``int``): The receiver id

        Returns:
            ``bool``: True if the conversation was cleared

        Raises:
            ``~switch.error.SwitchError``: If the conversation could not be cleared
        """
        log.debug("Clearing conversation %s", receiver_id)
        response = await self.client.get(
            f"{BASE_PATH}/clearconversationwith/{receiver_id}"
        )
        return True

    async def get_flag_messages(self, user_id: int = None) -> List[Message]:
        """Get flagged messages

        Parameters:
            user_id (``int``, *optional*): The user id. Defaults to the current user id.

        Returns:
            ``List[~switch.api.chat.models.Message]``: The flagged messages

        Raises:
            ``~switch.error.SwitchError``: If the flagged messages could not be retrieved
        """
        if user_id is None:
            user_id = self.client.user.id

        log.debug("Get flag messages for %s", user_id)
        response = await self.client.get(f"{BASE_PATH}/flag?userId={user_id}")
        return self.client.build_list(Message, response.data)
        # return Message.build_from_json_list(response.data)

    async def flag_message(self, message: Message | int) -> bool:
        """Flag a message

        Parameters:
            message (``~switch.api.chat.models.Message`` | ``int``): The message to flag

        Returns:
            ``bool``: True if the message was flagged

        Raises:
            ``~switch.error.SwitchError``: If the message could not be flagged
        """
        if isinstance(message, Message):
            message_id = message.id
        else:
            message_id = message
        log.debug("Flagging message %s", message_id)
        response = await self.client.post(f"{BASE_PATH}/flag?messageId={message_id}")
        return True

    async def get_unread_messages_count(self, user_id: int = None) -> int:
        """Get unread messages

        Parameters:
            user_id (``int``, *optional*): The user id. Defaults to the current user id.

        Returns:
            ``int``: The unread messages count
        """
        if user_id is None:
            user_id = self.client.user.id

        log.debug("Get unread messages count for %s", user_id)
        response = await self.client.get(
            f"{BASE_PATH}/unread-messages?userId={user_id}"
        )
        return response.data

    async def answer_inline_query(
        self, query: InlineQuery, answer: InlineQueryAnswer
    ) -> bool:
        """Answer an inline query

        Parameters:
            query (``~switch.api.chat.models.InlineQuery``): The inline query
            answer (``~switch.api.chat.models.InlineQueryAnser``): The answer

        Returns:
            ``bool``: True if the query was answered

        Raises:
            ``~switch.error.SwitchError``: If the query could not be answered
        """
        if not isinstance(query, InlineQuery):
            raise TypeError("query must be an InlineQuery instance")

        if isinstance(answer, str):
            answer = InlineQueryAnswer(
                query_id=query.query_id,
                title=answer,
                results=[],
                cache_time=0,
                is_personal=True,
                next_offset=None,
                pm_text=None,
                pm_parameter=None,
                user_id=query.user_id,
            )

        if isinstance(answer, List):
            answer = InlineQueryAnswer(
                query_id=query.query_id,
                title=None,
                results=answer,
                cache_time=0,
                is_personal=True,
                next_offset=None,
                pm_text=None,
                pm_parameter=None,
                user_id=query.user_id,
            )

        if not answer.user_id:
            answer.user_id = query.user_id

        log.debug("Answering inline query %s", query.query_id)
        response = await self.client.post(
            f"{BASE_PATH}/inline/answer", answer.to_json_request()
        )
        return response.data

    async def get_user(self, user_id: int | str = None) -> User:
        """Get user from user id"""
        response = await self.client.get(f"{BASE_PATH}/user/info?userId={user_id}")
        return self.client.build_object(User, response.data)
