from asyncio import gather, get_running_loop, AbstractEventLoop
from typing import TypeVar, Optional
from collections.abc import Callable, Awaitable, Iterable

InputType = TypeVar('InputType')
OutputType = TypeVar('OutputType')


async def map_and_gather(
    func: Callable[[InputType], Awaitable[OutputType]],
    input_data: Iterable[InputType]
) -> Iterable[OutputType]:
    return await gather(*[
        func(i)
        for i in input_data
    ])


def get_loop(loop: Optional[AbstractEventLoop]) -> AbstractEventLoop:
    if loop is None:
        return get_running_loop()

    return loop
