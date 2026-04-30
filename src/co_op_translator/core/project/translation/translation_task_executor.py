from __future__ import annotations

import asyncio
import logging

from tqdm import tqdm

from co_op_translator.utils.common.task_utils import worker

logger = logging.getLogger(__name__)


class TranslationTaskExecutorMixin:
    async def process_api_requests_parallel(self, tasks, task_desc) -> list:
        """Execute multiple API requests concurrently with controlled parallelism.

        Uses a queue system to manage API requests efficiently while providing
        progress feedback.

        Args:
            tasks: List of task functions to execute
            task_desc: Description for progress display

        Returns:
            List of results from completed tasks
        """
        if not tasks:  # No tasks to process
            logger.warning("No tasks available for processing.")
            return []

        task_queue = asyncio.Queue()

        # Initialize queue with all translation tasks
        for task in tasks:
            task_queue.put_nowait(task)

        # Add sentinel values so workers can exit cleanly after processing tasks
        worker_count = 5
        for _ in range(worker_count):
            task_queue.put_nowait(None)

        # Setup progress tracking UI
        with tqdm(total=len(tasks), desc=task_desc) as progress_bar:
            # Launch parallel worker tasks for processing
            workers = [
                asyncio.create_task(worker(task_queue, progress_bar))
                for _ in range(worker_count)
            ]

            # Wait for all queued tasks to complete
            await task_queue.join()

            # Gather worker completion to avoid InvalidStateError from unfinished tasks
            results = [t.result() for t in workers]

        return results

    async def process_api_requests_sequential(
        self, tasks, task_desc, file_names=None
    ) -> list:
        """Execute API requests one at a time in sequence.

        Ensures requests are processed in order while providing progress feedback.

        Args:
            tasks: List of task functions to execute
            task_desc: Description for progress display

        Returns:
            List of results from completed tasks
        """
        if not tasks:  # No tasks to process
            logger.warning("No tasks available for processing.")
            return []

        total_tasks = len(tasks)

        results = []
        with tqdm(total=total_tasks, desc=task_desc) as progress_bar:
            for i, task in enumerate(tasks):
                # Show current file name in progress bar if available
                if file_names and i < len(file_names):
                    file_name = file_names[i]
                    progress_bar.set_description(f"🔄 Translating: {file_name}")

                # Execute task and get result
                result = await task()  # Execute each task sequentially
                results.append(result)

                # Update progress bar
                progress_bar.update(1)

                # Reset description after completion if needed
                if i + 1 < total_tasks:
                    progress_bar.set_description(task_desc)

        return results
