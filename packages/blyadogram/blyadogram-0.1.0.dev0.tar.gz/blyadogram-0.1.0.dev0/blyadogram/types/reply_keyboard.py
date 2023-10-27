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


@dataclass
class KeyboardButton:
    text: str


class ReplyKeyboardMarkup:
    def __init__(self, resize_keyboard: bool = True, one_time_keyboard: bool = False):
        self.buttons = []
        self.reply_markup = json.dumps(
            {
                "keyboard": self.buttons,
                "resize_keyboard": resize_keyboard,
                "one_time_keyboard": one_time_keyboard,
            }
        )

    def add_button(self, button: KeyboardButton):
        self.buttons.append([{"text": button.text}])
        reply_markup = json.loads(self.reply_markup)
        reply_markup["keyboard"] = self.buttons
        self.reply_markup = json.dumps(reply_markup)

    def add_buttons(self, *buttons: KeyboardButton):
        for button in buttons:
            self.add_button(button)


class ReplyKeyboardRemove:
    reply_markup = json.dumps({"remove_keyboard": True})
