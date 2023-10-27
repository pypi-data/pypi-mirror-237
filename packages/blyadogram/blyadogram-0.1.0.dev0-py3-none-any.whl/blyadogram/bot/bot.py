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

from typing import Literal, Optional, Union

from ..database.base import Database
from ..types.chat import Chat
from ..types.inline_keyboard import InlineKeyboardMarkup
from ..types.input_file import InputFile
from ..types.message import Message
from ..types.reply_keyboard import ReplyKeyboardMarkup, ReplyKeyboardRemove
from ..types.user import User
from .methods import Methods


class Bot:
    def __init__(
        self,
        token: str,
        parse_mode: Optional[Literal["HTML", "MARKDOWN"]] = None,
        database: Optional[Database] = None,
    ):
        self.token = token
        self.parse_mode = parse_mode
        self.methods = Methods(bot=self)
        self.session = self.methods.session
        self.database = database

    async def connect_database(self, database: Database) -> None:
        self.database = database

    async def send_all(
        self,
        text: str,
        parse_mode: Optional[Literal["HTML", "MARKDOWN"]] = None,
        reply_markup: Union[
            ReplyKeyboardMarkup, InlineKeyboardMarkup, ReplyKeyboardRemove
        ] = ReplyKeyboardMarkup(),
    ) -> dict:
        number = 0
        users = await self.database.get_users()
        for user in users:
            await self.send_message(
                chat_id=user.id,
                text=text,
                parse_mode=parse_mode,
                reply_markup=reply_markup,
            )
            number += 1
        return {"successfully_sent": number, "error": len(users) - number}

    async def send_message(
        self,
        chat_id: Union[int, str],
        text: str,
        parse_mode: Optional[Literal["HTML", "MARKDOWN"]] = None,
        reply_markup: Union[
            ReplyKeyboardMarkup, InlineKeyboardMarkup, ReplyKeyboardRemove
        ] = ReplyKeyboardMarkup(),
    ) -> Message:
        return await self.methods.SendMessage(
            chat_id,
            text,
            reply_markup.reply_markup,
            parse_mode=parse_mode if parse_mode else self.parse_mode,
        )

    async def edit_message_text(
        self,
        chat_id: Union[int, str],
        text: str,
        message_id: int,
        parse_mode: str,
        reply_markup: InlineKeyboardMarkup = InlineKeyboardMarkup(),
    ) -> Message:
        return await self.methods.EditMessageText(
            chat_id=chat_id,
            text=text,
            message_id=message_id,
            reply_markup=reply_markup.reply_markup,
            parse_mode=parse_mode if parse_mode else self.parse_mode,
        )

    async def send_photo(
        self,
        chat_id: Union[int, str],
        photo: Union[InputFile, str],
        caption: Optional[str] = None,
        parse_mode: Optional[Literal["HTML", "MARKDOWN"]] = None,
        reply_markup: Union[
            ReplyKeyboardMarkup, InlineKeyboardMarkup, ReplyKeyboardRemove
        ] = ReplyKeyboardMarkup(),
    ) -> Message:
        return await self.methods.SendPhoto(
            chat_id=chat_id,
            photo=photo,
            caption=caption,
            parse_mode=parse_mode if parse_mode else self.parse_mode,
            reply_markup=reply_markup.reply_markup,
        )

    async def get_me(self) -> User:
        return await self.methods.GetMe()

    async def get_updates(
        self, allowed_updates: list | None, offset: Optional[int] = None
    ):
        return await self.methods.GetUpdates(offset, allowed_updates=allowed_updates)

    async def skip_updates(self):
        return await self.methods.SkipUpdates()

    async def answer_callback_query(
        self, callback_query_id: int, text: str, show_alert: bool = False
    ):
        return await self.methods.AnswerCallbackQuery(
            callback_query_id, text, show_alert
        )

    async def delete_message(self, chat_id: int, message_id: int):
        return await self.methods.DeleteMessage(chat_id=chat_id, message_id=message_id)

    async def get_chat(self, chat_id: int) -> Chat:
        return await self.methods.GetChat(chat_id=chat_id)
