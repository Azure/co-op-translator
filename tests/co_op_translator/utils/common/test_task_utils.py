"""
Test cases for task utility functions.
"""

import asyncio
import pytest
from unittest.mock import AsyncMock, MagicMock
from co_op_translator.utils.common.task_utils import worker


@pytest.mark.asyncio
async def test_worker_processes_tasks():
    """Test that worker processes tasks from queue."""
    # Create a mock task queue
    task_queue = asyncio.Queue()

    # Create async mock tasks
    async def mock_task():
        return True

    mock_tasks = [AsyncMock(wraps=mock_task) for _ in range(3)]
    for task in mock_tasks:
        await task_queue.put(task)
    await task_queue.put(None)  # Sentinel to stop the worker

    # Create a mock progress bar
    mock_progress = MagicMock()

    # Run the worker
    await worker(task_queue, mock_progress)

    # Verify all tasks were processed
    assert task_queue.empty()
    for task in mock_tasks:
        task.assert_awaited_once()


@pytest.mark.asyncio
async def test_worker_handles_empty_queue():
    """Test that worker handles empty queue correctly."""
    task_queue = asyncio.Queue()

    # Create a valid async task
    async def mock_task():
        return True

    mock = AsyncMock(wraps=mock_task)
    await task_queue.put(mock)
    await task_queue.put(None)  # Sentinel to stop the worker

    # Run the worker without progress bar
    await worker(task_queue)

    # Verify the queue is empty and task was called
    assert task_queue.empty()
    mock.assert_awaited_once()


@pytest.mark.asyncio
async def test_worker_handles_task_error():
    """Test that worker handles task errors gracefully."""
    task_queue = asyncio.Queue()

    # Create a mock task that raises an exception
    async def failing_task():
        raise ValueError("Task failed")

    mock = AsyncMock(wraps=failing_task)
    await task_queue.put(mock)
    await task_queue.put(None)  # Sentinel to stop the worker

    # Run the worker
    await worker(task_queue)

    # Verify the queue is empty despite the error
    assert task_queue.empty()
    mock.assert_awaited_once()
