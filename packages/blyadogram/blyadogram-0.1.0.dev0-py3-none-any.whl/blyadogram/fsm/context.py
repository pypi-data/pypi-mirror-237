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

from .state import State
from .storage.base import BaseStorage, UserKey


class FSMContext:
    def __init__(self, key: UserKey, storage: BaseStorage):
        self.key = key
        self.storage = storage

    async def set_state(self, state: State | None) -> None:
        return await self.storage.set_state(key=self.key, state=state)

    async def get_state(self) -> State:
        return await self.storage.get_state(key=self.key)

    async def get_data(self) -> dict:
        return await self.storage.get_data(self.key)

    async def set_data(self, data: dict) -> dict:
        return await self.storage.set_data(key=self.key, data=data)

    async def update_data(self, **data) -> dict:
        current_data = await self.get_data()
        current_data.update(data)
        await self.set_data(current_data)
        return current_data.copy()

    async def clear(self) -> None:
        await self.set_state(state=None)
        await self.set_data(data={})
