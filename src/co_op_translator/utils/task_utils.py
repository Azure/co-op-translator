import asyncio
from tqdm.asyncio import tqdm_asyncio

async def worker(task_queue: asyncio.Queue, progress_bar=None):
    """
    Worker function that processes tasks from the task queue, with optional progress bar updates.

    Args:
        task_queue (asyncio.Queue): The queue holding tasks to be processed.
        progress_bar (tqdm.asyncio.tqdm_asyncio, optional): The progress bar to update after each task.
    """
    while not task_queue.empty():
        task = await task_queue.get()  # Get the next task
        await task  # Process the task
        task_queue.task_done()  # Mark task as done

        # If a progress bar is provided, update it after each task
        if progress_bar:
            progress_bar.update(1)

async def queue_tasks(tasks: list, max_concurrent_tasks: int, task_desc: str = "Processing tasks"):
    """
    Queue tasks into an asyncio.Queue and process them using a limited number of concurrent workers.

    Args:
        tasks (list): List of coroutines representing tasks to be queued.
        max_concurrent_tasks (int): Maximum number of concurrent workers to process the tasks.
        task_desc (str): Description for the progress bar.
    """
    task_queue = asyncio.Queue()
    
    # Add tasks to the queue
    for task in tasks:
        task_queue.put_nowait(task)

    # Create a progress bar for tracking the task progress
    with tqdm_asyncio.tqdm_asyncio(total=len(tasks), desc=task_desc) as progress_bar:
        # Create worker tasks to process the queue concurrently
        workers = [asyncio.create_task(worker(task_queue, progress_bar)) for _ in range(max_concurrent_tasks)]

        # Wait until all tasks in the queue are processed
        await task_queue.join()

        # Ensure all workers have completed
        for worker_task in workers:
            worker_task.cancel()
