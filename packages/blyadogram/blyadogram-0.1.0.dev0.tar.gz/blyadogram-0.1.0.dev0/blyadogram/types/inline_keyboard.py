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
from dataclasses import dataclass
from typing import Optional


@dataclass
class InlineKeyboardButton:
    text: str
    callback_data: str = None
    url: str = None


def get_button(button: InlineKeyboardButton):
    but = {"text": button.text}
    param = (
        {"callback_data": button.callback_data}
        if button.callback_data
        else {"url": button.url}
    )
    but.update(param)
    return but


class InlineKeyboardMarkup:
    def __init__(self, inline_keyboard: Optional[list["InlineKeyboardButton"]] = None):
        self.buttons: list["InlineKeyboardButton"] = (
            []
            if not inline_keyboard
            else [get_button(but[0]) for but in inline_keyboard]
        )

    @property
    def reply_markup(self) -> str:
        return json.dumps({"inline_keyboard": self.buttons})

    def add_button(self, button: InlineKeyboardButton):
        if (
            button.url is not None
            and button.callback_data is None
            or button.url is None
            and button.callback_data is not None
        ):
            button = get_button(button)
            self.buttons.append([button])
        else:
            raise ValueError(
                "Inline Keyboard Button must to have a callback_data or url."
            )

    def add_buttons(self, *buttons: InlineKeyboardButton):
        for button in buttons:
            self.add_button(button)
