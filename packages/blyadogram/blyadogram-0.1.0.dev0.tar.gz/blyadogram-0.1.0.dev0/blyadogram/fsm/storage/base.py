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

from abc import ABC, abstractmethod
from dataclasses import dataclass

from ..state import State


@dataclass(frozen=True)
class UserKey:
    chat_id: int
    user_id: int


class BaseStorage(ABC):
    @abstractmethod
    async def set_state(self, key: UserKey, state: State) -> None:
        pass

    @abstractmethod
    async def get_state(self, key: UserKey) -> State:
        pass

    @abstractmethod
    async def get_data(self, key: UserKey) -> dict:
        pass

    @abstractmethod
    async def set_data(self, key: UserKey, data: dict) -> dict:
        pass
