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

from .base import BaseMiddleware


class HandlerMiddlewares:
    def __init__(
        self,
        func: callable,
        data: dict,
        args: list,
        update,
        middlewares: list[BaseMiddleware],
    ):
        self.func = func
        self.args = args
        self.update = update
        self.middlewares = middlewares
        self.data = data
        self.number = 0

    async def __call__(self):
        self.number += 1
        if self.number == len(self.middlewares):
            for key in [key for key in self.data.keys()]:
                if key not in self.args:
                    self.data.pop(key)
            await self.func(self.update, **self.data)

    async def start(self):
        for middleware in self.middlewares:
            await middleware(handler=self, update=self.update, data=self.data)
