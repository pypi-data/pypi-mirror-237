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

import json
from typing import Literal, Optional

from redis.asyncio.client import ConnectionPool, Redis

from ..state import State
from .base import BaseStorage, UserKey


def build_key(key: UserKey, build_name: Literal["state", "data"]) -> str:
    redis_key = "USER" + build_name + str(key.chat_id) + ":" + str(key.user_id)
    return redis_key


class RedisStorage(BaseStorage):
    def __init__(
        self,
        redis: Optional[Redis] = None,
        host: str = "localhost",
        port: int = 6379,
        db: int = 0,
        password: Optional[str] = None,
    ):
        self.redis = (
            Redis(host=host, port=port, db=db, password=password)
            if not redis
            else redis
        )

    @classmethod
    def from_url(cls, url: str):
        pool = ConnectionPool.from_url(url=url)
        redis = Redis(connection_pool=pool)
        return cls(redis=redis)

    async def set_state(self, key: UserKey, state: State | None) -> None:
        await self.redis.set(name=build_key(key, "state"), value=state.__str__())

    async def get_state(self, key: UserKey) -> State:
        value = (await self.redis.get(name=build_key(key, "state"))).decode("utf-8")
        if value == "None":
            value = None
        return value

    async def set_data(self, key: UserKey, data: dict) -> dict:
        await self.redis.set(name=build_key(key, "data"), value=json.dumps(data))
        return data.copy()

    async def get_data(self, key: UserKey) -> dict:
        value = await self.redis.get(name=build_key(key, "data"))
        if isinstance(value, bytes):
            value = value.decode("utf-8")
            if value == "None":
                value = json.dumps({})
        else:
            value = json.dumps({})
        data = json.loads(value)
        return data

    async def close(self):
        await self.redis.close()
