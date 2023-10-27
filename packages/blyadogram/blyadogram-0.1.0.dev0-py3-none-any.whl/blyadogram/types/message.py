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
from typing import Any, Literal, Optional, Union

from blyadogram.types.inline_keyboard import InlineKeyboardMarkup
from blyadogram.types.reply_keyboard import (ReplyKeyboardMarkup,
                                             ReplyKeyboardRemove)

from ..types.chat import Chat
from ..types.photo import PhotoSize
from ..types.user import User
from .input_file import InputFile


@dataclass
class Message:
    bot: Any
    message_id: int
    chat: Chat
    from_user: User
    date: int
    text: str = None
    caption: str = None
    photo: list[PhotoSize] = None
    entities: list = None
    edit_date: int = None
    reply_markup: InlineKeyboardMarkup = None

    async def answer(
        self,
        text: str,
        parse_mode: Optional[str] = None,
        reply_markup: Union[
            ReplyKeyboardMarkup, InlineKeyboardMarkup, ReplyKeyboardRemove
        ] = ReplyKeyboardMarkup(),
    ) -> "Message":
        return await self.bot.send_message(
            chat_id=self.chat.id,
            text=text,
            parse_mode=parse_mode,
            reply_markup=reply_markup,
        )

    async def answer_photo(
        self,
        photo: Union[InputFile, str],
        caption: Optional[str] = None,
        parse_mode: Optional[Literal["HTML", "MARKDOWN"]] = None,
        reply_markup: Union[
            ReplyKeyboardMarkup, InlineKeyboardMarkup, ReplyKeyboardRemove
        ] = ReplyKeyboardMarkup(),
    ) -> "Message":
        return await self.bot.send_photo(
            chat_id=self.chat.id,
            photo=photo,
            caption=caption,
            parse_mode=parse_mode,
            reply_markup=reply_markup,
        )

    async def delete(self):
        return await self.bot.delete_message(
            chat_id=self.chat.id, message_id=self.message_id
        )

    async def edit_text(
        self,
        text: str,
        reply_markup: InlineKeyboardMarkup = InlineKeyboardMarkup(),
        parse_mode: Optional[str] = None,
    ) -> "Message":
        return await self.bot.edit_message_text(
            chat_id=self.chat.id,
            text=text,
            message_id=self.message_id,
            parse_mode=parse_mode,
            reply_markup=reply_markup,
        )
