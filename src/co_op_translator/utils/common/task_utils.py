import asyncio
from tqdm.asyncio import tqdm_asyncio
import logging

logger = logging.getLogger(__name__)


async def worker(task_queue: asyncio.Queue, progress_bar=None):
    """
    Worker function that processes tasks from the task queue, with optional progress bar updates.

    Args:
        task_queue (asyncio.Queue): The queue holding tasks to be processed.
        progress_bar (tqdm.asyncio.tqdm_asyncio, optional): The progress bar to update after each task.
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

    # 3) Create a progress bar with total == number of real tasks
    with tqdm_asyncio.tqdm_asyncio(total=len(tasks), desc=task_desc) as progress_bar:
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
