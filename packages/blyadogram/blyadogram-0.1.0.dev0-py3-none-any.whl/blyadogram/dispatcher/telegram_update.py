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

from ..filters.base import BaseFilter
from ..middlewares.base import BaseMiddleware


@dataclass
class Handler:
    func: callable
    update: str
    filters: list
    middlewares: list


class TelegramUpdate:
    def __init__(self, router, update: str):
        self.router = router
        self.update = update
        self._filters = []
        self._middlewares = []

    def register_middleware(self, middleware: BaseMiddleware):
        self._middlewares.append(middleware)

    def register(self, handler: callable, *filters: BaseFilter):
        filters = [filter for filter in filters]
        filters.extend(self._filters)
        self.router.handlers.append(
            Handler(
                func=handler,
                update=self.update,
                filters=filters,
                middlewares=self._middlewares,
            )
        )

    def filter(self, filter: BaseFilter):
        self._filters.append(filter)

    def __call__(self, *filters: BaseFilter):
        def wrapper(func):
            self.register(func, *filters)

        return wrapper
