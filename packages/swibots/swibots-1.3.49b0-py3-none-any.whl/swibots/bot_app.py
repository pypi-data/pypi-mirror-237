import os
import asyncio
import logging
from typing import List, Collection, Optional
import swibots
from importlib import import_module
from swibots.api.community.events import CommunityEvent
from swibots.api.chat.events import ChatEvent
from swibots.bots import BotContext, Decorators, BaseHandler
from swibots.api.bot.models import BotInfo, BotCommandInfo
from swibots.api.common.events import Event
from .app import App

log = logging.getLogger(f"{__name__}")
LoaderLog = logging.getLogger("loader")


class BotApp(App, Decorators):
    """Bot client

    This is the main class for interacting with the Switch BOT API.

    """

    def __init__(
        self,
        # username: Optional[str] = None,
        # password: Optional[str] = None,
        token: Optional[str] = None,
        bot_description: Optional[str] = None,
        auto_update_bot: Optional[bool] = True,
        loop: asyncio.AbstractEventLoop = None,
        receive_updates: Optional[bool] = True
        #        plugins: Optional[List[str]] = None,
    ):
        """
        Initialize the client

        Args:
            token (:obj:`str`): The bot token.
            bot_description(:obj:`str`): The bot description.
            auto_update_bot(:obj:`bool`): Whether to automatically update the bot description and the regitered commands.
            loop (:obj:`asyncio.AbstractEventLoop`): The asyncio loop to use (default: asyncio.get_event_loop()).

        """
        super().__init__(token, loop, receive_updates)
        self._user_type = swibots.bots.Bot
        self._botinfo: BotInfo = None
        self.on_chat_service_start = self._on_chat_service_start
        self.on_community_service_start = self._on_community_service_start
        self._handlers: List[BaseHandler] = []
        self._register_commands: List[swibots.bots.RegisterCommand] = []
        self._bot_description = bot_description
        #        self._plugins = plugins
        self.auto_update_bot = auto_update_bot
        self.user = self._loop.run_until_complete(self.get_me(user_type=self._user_type))
        self._bot_id = self.user.id

    @property
    def bot(self) -> "swibots.bots.Bot":
        """
        The bot user.

            Returns:
                :obj:`swibots.bots.Bot`: The bot user.
        """
        return self.user

    @property
    def handlers(self) -> List[BaseHandler]:
        """
        Get the list of handlers.

        Returns:
            :obj:`List[BaseHandler]`: The list of handlers.
        """
        if self._handlers is None:
            self._handlers = []
        return self._handlers

    def __loadModule(self, path):
        baseName = os.path.basename(path)
        if baseName.startswith("__") or not baseName.endswith(".py"):
            return
        try:
            module_path = path[:-3].replace("\\", ".").replace("/", ".")

            return import_module(module_path)
        except Exception as er:
            LoaderLog.exception(er)

    def load_plugins(self, plugins: List[str]):
        for path in plugins:
            if os.path.isfile(path):
                self.__loadModule(path)
                return
            for root, __, files in os.walk(path):
                for f in files:
                    self.__loadModule(os.path.join(root, f))

    def register_command(
        self, command: swibots.bots.RegisterCommand | List[swibots.bots.RegisterCommand]
    ) -> "BotApp":
        if isinstance(command, list):
            self._register_commands.extend(command)
        else:
            self._register_commands.append(command)
        self._loop.create_task(self.update_bot_commands())
        return self

    def unregister_command(
        self, command: swibots.bots.RegisterCommand | List[swibots.bots.RegisterCommand]
    ) -> "BotApp":
        if isinstance(command, list):
            for cmd in command:
                self._register_commands.remove(cmd)
        else:
            self._register_commands.remove(command)
        self._loop.create_task(self.update_bot_commands())
        return self

    def add_handler(self, handler: BaseHandler | List[BaseHandler]) -> "BotApp":
        if isinstance(handler, list):
            self.handlers.extend(handler)
        else:
            self.handlers.append(handler)
        return self

    def remove_handler(self, handler: BaseHandler | List[BaseHandler]) -> "BotApp":
        if not isinstance(handler, list):
            handler = [handler]
        for h in handler:
            self.handlers.remove(h)
        return self

    async def update_bot_commands(self):
        # get all app commands
        commands = self._register_commands or []
        description = self._bot_description or ""
        # register the commands
        self._botinfo = BotInfo(description=description, id=self._bot_id)
        for command in commands:
            command_name = command.command
            if isinstance(command_name, str):
                command_names = command_name.split(",")
            else: 
                command_names = command_name

            for c_name in command_names:
                self._botinfo.commands.append(
                    BotCommandInfo(
                        command=c_name,
                        description=command.description,
                        channel=command.channel,
                    )
                )

        self._botinfo = await self.update_bot_info(self._botinfo)

    async def _validate_token(self):
        await super()._validate_token()
        if not isinstance(self.user, self._user_type):
            raise swibots.SwitchError("Invalid token")

        if not self.user.is_bot:
            raise swibots.SwitchError("Invalid token (not a bot)")

        self.user.app = self
        # Register commands
        await self.user.on_app_start(self)

    async def _on_chat_service_start(self, _):
        await self.chat_service.subscribe_to_notifications(callback=self.on_chat_event)

    async def _on_community_service_start(self, _):
        await self.community_service.subscribe_to_notifications(
            callback=self.on_community_event
        )

    def _build_context(self, event: Event) -> BotContext:
        return BotContext(bot=self.bot, event=event)

    async def process_event(self, ctx: BotContext):
        for handler in self.handlers:
            if await handler.should_handle(ctx):
                try:
                    await handler.handle(ctx)
                except Exception as e:
                    log.exception(f"Error while processing event: {e}")
                    raise e
                finally:
                    break

    async def on_community_event(self, evt: CommunityEvent):
        if evt is not None and isinstance(evt, Event):
            await self.process_event(self._build_context(evt))

    async def on_chat_event(self, evt: ChatEvent):
        if evt is not None:
            await self.process_event(self._build_context(evt))
