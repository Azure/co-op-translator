from __future__ import annotations

import asyncio
import logging

from co_op_translator.utils.common.task_utils import worker
from co_op_translator.utils.common.progress import get_progress_reporter

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

        reporter = get_progress_reporter()

        # Setup progress tracking UI
        with reporter.task(task_desc, total=len(tasks), unit="request") as progress_bar:
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
        self,
        tasks,
        task_desc,
        file_names=None,
        file_info=None,
        stage_key: str | None = None,
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

        reporter = get_progress_reporter()

        results = []
        with reporter.task(
            task_desc, total=total_tasks, unit="request", stage_key=stage_key
        ) as progress_bar:
            for i, task in enumerate(tasks):
                # Show current file name in progress bar if available
                current_path = None
                current_language = None
                if file_info and i < len(file_info):
                    current_path, current_language = file_info[i]
                    progress_bar.file_started(current_path, current_language)
                if file_names and i < len(file_names):
                    file_name = file_names[i]
                    progress_bar.set_detail(f"Current: {file_name}")

                # Execute task and get result
                result = await task()  # Execute each task sequentially
                results.append(result)

                # Update progress bar
                progress_bar.update(1)
                if current_path is not None:
                    if result:
                        progress_bar.file_completed(current_path, current_language)
                    else:
                        progress_bar.file_failed(
                            current_path,
                            current_language,
                            message=f"Failed to process {current_path}",
                        )

                # Reset description after completion if needed
                if i + 1 < total_tasks:
                    progress_bar.set_description(task_desc)

        return results
