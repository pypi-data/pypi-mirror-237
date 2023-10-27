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
import warnings


from datetime import datetime, timedelta
from dataclasses import dataclass

def info():
    warnings.warn("СУКА ИСПОЛЬЗУЙ NATS!!!\n YOU MUST USE NATS FOR MAILING")

@dataclass
class Job:
    func: callable
    run_date: datetime
    number_repetitions: int
    interval_time: timedelta
    is_forever: bool
    kwargs: dict


class BlyadoScheduler:
    def __init__(self):
        info()
        self.jobs: list[Job] = []

    def add_job(self, func: callable, run_date: datetime = datetime.now(), number_repetitions: int = 1, interval_time: timedelta = timedelta(seconds=0.5), is_forever: bool = False, kwargs: dict = dict):
        info()
        self.jobs.append(Job(func=func, run_date=run_date, number_repetitions=number_repetitions, interval_time=interval_time, is_forever=is_forever, kwargs=kwargs))

    async def remove_jobs(self):
        info()
        self.jobs.clear()

    async def start(self, dispatcher):
        while dispatcher.keep_polling is True:
            await asyncio.sleep(1)
            if self.jobs:
                info()
                await asyncio.wait([asyncio.create_task(self._run(job=job)) for job in self.jobs])
                task_1 = asyncio.create_task(self.remove_jobs())
                task_2 = asyncio.create_task(self.start(dispatcher=dispatcher))
                await task_1
                await task_2
                break

    async def _run(self, job: Job):
        await asyncio.sleep((job.run_date - datetime.now()).total_seconds())
        number = 0
        while number < job.number_repetitions if job.is_forever is False else True:
            info()
            await job.func(**job.kwargs)
            await asyncio.sleep(job.interval_time.total_seconds())
            number += 1
        
