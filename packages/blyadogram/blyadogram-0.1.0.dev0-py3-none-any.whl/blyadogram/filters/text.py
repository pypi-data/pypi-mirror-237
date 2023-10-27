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

from typing import Optional

from ..exceptions import FilterError
from ..types.message import Message
from .base import BaseFilter


class Text(BaseFilter):
    def __init__(
        self,
        text: Optional[str] = None,
        startswith: Optional[str] = None,
        endswith: Optional[str] = None,
    ):
        if (
            text
            and startswith is None
            and endswith is None
            or startswith
            and text is None
            or endswith
            and text is None
        ):
            self.text = text
            self.startswith = startswith
            self.endswith = endswith
        else:
            raise FilterError(message="Filter Text most have a one argument.")

    async def __check__(self, message: Message) -> bool:
        if self.text is not None:
            return message.text == self.text
        elif self.startswith is not None:
            return message.text.startswith(self.startswith)
        else:
            return message.text.endswith(self.endswith)
