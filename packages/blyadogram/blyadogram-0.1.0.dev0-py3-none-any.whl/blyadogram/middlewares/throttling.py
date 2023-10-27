"""
 Copyright (c) 2023 DiorDS

 Permission is hereby granted, free of charge, to any person obtaining a copy of
 this software and associated documentation files (the "Software"), to deal in
 the Software without restriction, including without limitation the rights to
 use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
 the Software, and to permit persons to whom the Software is furnished to do so,
 subject to the following conditions:

 The above copyright notice and this permission notice shall be included in all
 copies or substantial portions of the Software.

 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
 FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
 COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
 IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
 CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
 """

from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Any, Awaitable, Callable

from ..types import Message
from .base import BaseMiddleware


@dataclass(frozen=True)
class UserKey:
    chat_id: int
    user_id: int


@dataclass
class DataKey:
    date: datetime
    is_message: bool


class ThrottlingMiddleware(BaseMiddleware):
    def __init__(self, delay: int = 3, message: str = "❗ Не так быстро."):
        self.delay = delay
        self.message = message
        self.storage: dict[UserKey, DataKey] = dict()

    async def __call__(self, handler: callable, update: Message, data: dict) -> Any:
        key = UserKey(chat_id=update.chat.id, user_id=update.from_user.id)
        if key in self.storage.keys():
            if datetime.now() - self.storage[key].date > timedelta(seconds=self.delay):
                self.storage.pop(key)
                return await handler()
            else:
                if self.storage[key].is_message is True:
                    self.storage[key].is_message = False
                    return await update.answer(text=self.message)
        else:
            self.storage[key] = DataKey(date=datetime.now(), is_message=True)
            return await handler()
