import asyncio
import logging
from collections.abc import Awaitable, Callable, Sequence
from typing import TypeVar, cast

from co_op_translator.utils.common.progress import get_progress_reporter

logger = logging.getLogger(__name__)
T = TypeVar("T")


def validate_concurrency(concurrency: int) -> None:
    """Reject invalid limits before starting work or initializing providers."""
    if (
        isinstance(concurrency, bool)
        or not isinstance(concurrency, int)
        or concurrency < 1
    ):
        raise ValueError("concurrency must be a positive integer")


async def run_tasks_concurrently(
    tasks: Sequence[Callable[[], Awaitable[T]]], concurrency: int = 1
) -> list[T]:
    """Run async factories with bounded workers and return results in input order.

    Factories defer coroutine creation until a worker is available. On failure or
    cancellation, cancel and drain all workers before propagating the exception.
    """
    validate_concurrency(concurrency)
    if concurrency == 1:
        return [await task() for task in tasks]

    results: list[T | None] = [None] * len(tasks)
    pending = iter(enumerate(tasks))

    async def run_worker() -> None:
        for index, task in pending:
            results[index] = await task()

    workers = [
        asyncio.create_task(run_worker()) for _ in range(min(concurrency, len(tasks)))
    ]
    try:
        await asyncio.gather(*workers)
    except BaseException:
        for worker_task in workers:
            worker_task.cancel()
        await asyncio.gather(*workers, return_exceptions=True)
        raise
    return cast(list[T], results)


async def worker(task_queue: asyncio.Queue, progress_bar=None):
    """
    Worker function that processes tasks from the task queue, with optional progress bar updates.

    Args:
        task_queue (asyncio.Queue): The queue holding tasks to be processed.
        progress_bar (ProgressTask, optional): The progress task to update after each task.
    """
    while True:
        task = await task_queue.get()
        if task is None:
            # Sentinel value to stop the worker
            task_queue.task_done()  # Mark the sentinel as done
            break

        try:
            # If 'task' is already a coroutine object, just await it.
            if asyncio.iscoroutine(task):
                await task
            # If 'task' is a coroutine function, call it then await it.
            elif asyncio.iscoroutinefunction(task):
                await task()
            else:
                # Otherwise, assume it's a regular callable that may block -> run in thread
                await asyncio.to_thread(task)

            # Update the progress bar for a successful task
            if progress_bar:
                progress_bar.update(1)

        except Exception as e:
            logger.error(f"Error processing task: {e}")

        finally:
            # No matter what happens, mark the task as done
            task_queue.task_done()


async def queue_tasks(
    tasks: list, max_concurrent_tasks=4, task_desc: str = "Processing tasks"
):
    """
    Queue tasks into an asyncio.Queue and process them using a limited number of concurrent workers.

    Args:
        tasks (list): List of coroutines representing tasks to be queued.
        max_concurrent_tasks (int): Maximum number of concurrent workers to process the tasks.
        task_desc (str): Description for the progress bar.
    """
    task_queue = asyncio.Queue()

    # 1) Enqueue all actual tasks
    for task in tasks:
        await task_queue.put(task)

    # 2) Add sentinel values to signal workers to exit once tasks are done
    for _ in range(max_concurrent_tasks):
        await task_queue.put(None)

    reporter = get_progress_reporter()

    # 3) Create a progress task with total == number of real tasks
    with reporter.task(task_desc, total=len(tasks), unit="task") as progress_bar:
        # Start workers
        workers = [
            asyncio.create_task(worker(task_queue, progress_bar))
            for _ in range(max_concurrent_tasks)
        ]

        # Wait for the queue to empty
        await task_queue.join()

        # Allow workers to finish
        for w in workers:
            await w
