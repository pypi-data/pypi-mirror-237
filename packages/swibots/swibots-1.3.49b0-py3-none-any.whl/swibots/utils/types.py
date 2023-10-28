import os, asyncio
from asyncio import create_task, run_coroutine_threadsafe, get_event_loop
from asyncio.exceptions import InvalidStateError
from enum import Enum
from typing import Any, Callable, Collection, Coroutine, Dict, TypeVar, Union
from inspect import iscoroutinefunction
from swibots.error import CancelError
from threading import Thread

class IOClient:
    def cancel(self) -> None:
        raise CancelError("called cancel()")


class DownloadProgress:
    def __init__(
        self, downloaded: int, total: int, url: str, client: IOClient, file_name: str
    ):
        self.downloaded = downloaded
        self.total = total
        self.url = url
        self.client = client
        self.file_name = file_name
        self.started = False


class UploadProgress:
    def __init__(
        self,
        path: str = None,
        callback=None,
        callback_args: tuple = (),
        client: IOClient = None,
        loop=None,
        readed=0,
        current=0,
    ) -> None:
        super().__init__()
        self.callback = callback
        self.path = path
        self.total = os.path.getsize(path)
        self.callback_args = callback_args
        self.readed = readed
        self.current = current
        self.client = client
        #self.bar = bar or tqdm(total=self.total, unit="B",
        #                       unit_scale=True, unit_divisor=1024)
    
    def update(self, bytes):
        self.current = bytes 
        self.readed += bytes
        self.runCallback(self.current)

    def bytes_completed(self, byte_count):
        if self.readed and byte_count > self.readed:
            self.current = byte_count - self.readed
        else:
            self.current = byte_count
        self.readed = byte_count
        self.runCallback(self.current)
    
    async def bytes_readed(self, length):
        self.current = length
        self.readed += length

        if self.callback:
            iscoro = self.callback(UploadProgress(self.path, self.callback, self.callback_args, self.client, readed=self.readed, current=length,
                                              
                                                  ), *self.callback_args or (),
                                   )
            if iscoroutinefunction(self.callback):
                asyncio.create_task(iscoro)

    def runCallback(self, current):

        if self.callback:
            iscoro = self.callback(UploadProgress(self.path, self.callback, self.callback_args, self.client, readed=self.readed, current=current,
                                                  #bar=self.bar
                                                  ), *self.callback_args or ())
            if iscoroutinefunction(self.callback):

                th = Thread(target=lambda: asyncio.run(iscoro))
                th.start()
        return
    
    def set_total_bytes(self, total):
        self.total = total

"""
class UploadProgress:
    def __init__(
        self,
        current: int,
        readed: int,
        url: str,
        client: IOClient,
        file_name: str,
        callback,
        callback_args,
    ):
        self.current = current
        self.readed = readed
        self.url = url
        self.client = client
        self.file_name = file_name
        self.started = False
        self.cancelled = False
        self.callback = callback
        self.callback_args = callback_args
        self._readable_file: ReadCallbackStream = None
        self._tasks = []

    def update(self, current: int) -> None:
        if self.cancelled:
            return
        self.current = current
        self.readed += current
        if self.callback:
            async def task():
                try:
                    iscoro = self.callback(self, *self.callback_args)
                    if iscoroutinefunction(self.callback):
                        await iscoro
                except CancelError as er:
                    self.cancelled = True
                    if self._readable_file:
                        self._readable_file.cancelled = True
                    return False
                return True
            loop = get_event_loop()
            _task = loop.create_task(task())
            self._tasks.append(_task)

            def onDone(task):
                if _task.exception():
                    if self._readable_file:
                        self._readable_file.cancelled = True

            _task.add_done_callback(onDone)
"""

CtxType = TypeVar("CtxType")
ResType = TypeVar("ResType")
HandlerCallback = Callable[[CtxType], Coroutine[Any, Any, ResType]]
FilterCallback = Callable[[CtxType], Coroutine[Any, Any, bool]]
DownloadProgressCallback = Callable[[DownloadProgress], Coroutine[Any, Any, None]]
UploadProgressCallback = Callable[[DownloadProgress], Coroutine[Any, Any, None]]

RT = TypeVar("RT")
SCT = Union[RT, Collection[RT]]
"""Single instance or collection of instances."""

JSONDict = Dict[str, Any]


class ReadCallbackStream(object):
    """Wraps a file-like object in another, but also calls a user
    callback with the number of bytes read whenever its `read()` method
    is called. Used for tracking upload progress, for example for a
    progress bar in a UI application. Idea taken from ActiveState Code Recipe:
    http://code.activestate.com/recipes/578669-wrap-a-string-in-a-file-like-object-that-calls-a-u/
    """

    def __init__(self, file_like, callback):
        if isinstance(file_like, str):
            self.file_like = open(file_like, "rb")
        else:
            self.file_like = file_like
        self.callback = callback
        self.cancelled = False
    
    def seek(self, arg):
        return self.file_like.seek(arg)

    def read(self, *args):
        if self.cancelled:
            raise CancelError("Task has been cancelled!")
        chunk = self.file_like.read(*args)
        if len(chunk) > 0:
            self.callback(len(chunk))
        return chunk

    def close(self):
        if hasattr(self.file_like, "close"):
            self.file_like.close()


class RequestMethod(Enum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    PATCH = "PATCH"
    DELETE = "DELETE"
