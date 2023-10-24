from abc import abstractmethod
from asyncio import AbstractEventLoop, Queue
from collections.abc import Callable, Awaitable, AsyncIterator
from contextlib import asynccontextmanager
from typing import Generic, Optional

from .utils import InputType, OutputType, get_loop


class WorkerBase(Generic[InputType, OutputType]):
    @abstractmethod
    async def handle(self, job: InputType) -> OutputType:
        raise NotImplementedError


class Pool(Generic[InputType, OutputType]):
    def __init__(
        self,
        worker_cls: type[WorkerBase[InputType, OutputType]],
        max_worker_count: int,
        loop: AbstractEventLoop,
    ):
        self.worker_cls = worker_cls
        self.max_worker_count = max_worker_count
        self.loop = loop

        # idle workers
        self._queue: Queue[WorkerBase[InputType, OutputType]] = Queue(
            maxsize=self.max_worker_count
        )

        # busy workers
        self._working: set[WorkerBase[InputType, OutputType]] = set()

    @property
    def size(self) -> int:
        return len(self._working) + self._queue.qsize()

    @property
    def is_full(self) -> bool:
        return self.size >= self.max_worker_count

    @asynccontextmanager
    async def acquire_worker(
        self
    ) -> AsyncIterator[WorkerBase[InputType, OutputType]]:
        worker = None

        try:
            if self.is_full:
                worker = await self._queue.get()
            else:
                worker = self._create_worker()

            self._working.add(worker)
            yield worker
        finally:
            if worker:
                self._working.remove(worker)
                await self._queue.put(worker)

    def _create_worker(self) -> WorkerBase[InputType, OutputType]:
        return self.worker_cls()


def run_in_pool(
    max_worker_count: int,
    loop: Optional[AbstractEventLoop],
) -> Callable[
    [Callable[[InputType], Awaitable[OutputType]]],
    Callable[[InputType], Awaitable[OutputType]]
]:
    def wrapper(
        func: Callable[[InputType], Awaitable[OutputType]]
    ) -> Callable[[InputType], Awaitable[OutputType]]:
        class _Worker(WorkerBase[InputType, OutputType]):
            async def handle(self, job: InputType) -> OutputType:
                return await func(job)

        return run_worker_in_pool(
            worker_cls=_Worker,
            max_worker_count=max_worker_count,
            loop=get_loop(loop),
        )

    return wrapper


def run_worker_in_pool(
    worker_cls: type[WorkerBase[InputType, OutputType]],
    max_worker_count: int,
    loop: AbstractEventLoop,
) -> Callable[[InputType], Awaitable[OutputType]]:
    pool = Pool(
        worker_cls=worker_cls,
        max_worker_count=max_worker_count,
        loop=loop,
    )

    async def wrapper(job: InputType) -> OutputType:
        async with pool.acquire_worker() as worker:
            return await worker.handle(job)

    return wrapper
