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

import asyncio
from pathlib import Path
from typing import Optional, Union

import aiosqlite
from aiosqlite import Connection, Cursor

from ..exceptions import DatabaseError
from ..types.user import User
from .base import Database


class SQLite3(Database):
    def __init__(self, connection: Connection):
        self.connection = connection
        asyncio.create_task(self.start())

    async def start(self):
        query = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER NOT NULL, first_name TEXT NOT NULL, last_name TEXT NOT NULL, username TEXT NOT NULL, is_bot TEXT NOT NULL)"
        await self.request(query=query)

    async def request(self, query: str, params: Optional[tuple] = None):
        await self.connection.execute(query, params)
        await self.connection.commit()

    async def select(
        self,
        table: str,
        columns: list[str] | str,
        params: Optional[dict] = None,
        fetch_all: bool = False,
        fetch_number: int = 1,
    ):
        cursor: Cursor = await self.connection.cursor()

        if isinstance(columns, list):
            take_columns = ""
            for column in columns:
                take_columns += column + ", "
            columns = take_columns[:-2]

        params_query = "WHERE " if params else None
        if params:
            for key, value in params.items():
                params_query += key + " = " + value + " "

        result = await cursor.execute(f"SELECT {columns} FROM {table} {params_query}")
        result = (
            await result.fetchmany(fetch_number)
            if fetch_all is False
            else await result.fetchall()
        )
        return result

    async def user_exist(self, user: User) -> bool:
        users = await self.get_users()
        return user in users

    async def add_user(self, user: User):
        if not await self.user_exist(user=user):
            try:
                await self.request(
                    query="INSERT INTO users (user_id, first_name, last_name, username, is_bot) VALUES (?, ?, ?, ?, ?)",
                    params=(
                        user.id,
                        user.first_name,
                        user.last_name.__str__(),
                        user.username,
                        user.is_bot.__str__(),
                    ),
                )
            except Exception as ex:
                raise DatabaseError(message=ex.__str__())

    async def get_users(self) -> list[User]:
        cursor: Cursor = await self.connection.cursor()
        result = await cursor.execute(
            "SELECT user_id, first_name, last_name, username, is_bot FROM users"
        )
        users_res = await result.fetchall()
        users = [
            User(
                id=user[0],
                first_name=user[1],
                last_name=user[2] if user[2] != "None" else None,
                username=user[3],
                is_bot=True if user[4] == "True" else False,
            )
            for user in users_res
        ]
        return users

    async def close(self):
        await self.connection.close()
