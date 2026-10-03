import asyncio
from functools import partial

import pytest

from co_op_translator.utils.common.task_utils import run_tasks_concurrently


@pytest.mark.asyncio
@pytest.mark.parametrize("limit", [1, 2, 10])
async def test_worker_limit_defers_factories_until_capacity_is_available(limit):
    started = []
    first_wave = asyncio.Event()
    release = asyncio.Event()
    active = peak = 0

    async def task(index):
        nonlocal active, peak
        started.append(index)
        active += 1
        peak = max(peak, active)
        if len(started) == min(limit, 5):
            first_wave.set()
        try:
            await release.wait()
            await asyncio.sleep(0)
            return index
        finally:
            active -= 1

    running = asyncio.create_task(
        run_tasks_concurrently([partial(task, i) for i in range(5)], limit)
    )
    try:
        await asyncio.wait_for(first_wave.wait(), 2)
        assert started == list(range(min(limit, 5)))
    finally:
        release.set()
        results = await asyncio.wait_for(running, 2)
    assert results == list(range(5))
    assert peak == min(limit, 5)
    assert active == 0


@pytest.mark.asyncio
async def test_results_keep_input_order_when_completion_order_differs():
    second_done = asyncio.Event()
    completed = []

    async def first():
        await second_done.wait()
        completed.append(0)
        return None

    async def second():
        completed.append(1)
        second_done.set()
        return False

    assert await run_tasks_concurrently([first, second], 2) == [None, False]
    assert completed == [1, 0]


@pytest.mark.asyncio
async def test_failure_cancels_and_drains_other_workers():
    partner_started = asyncio.Event()
    partner_cleaned = asyncio.Event()
    unexpected = []

    async def fail():
        await partner_started.wait()
        raise RuntimeError("provider failed")

    async def blocked():
        partner_started.set()
        try:
            await asyncio.Event().wait()
        finally:
            await asyncio.sleep(0)
            partner_cleaned.set()

    async def queued():
        unexpected.append(True)

    with pytest.raises(RuntimeError, match="provider failed"):
        await asyncio.wait_for(run_tasks_concurrently([fail, blocked, queued], 2), 2)
    assert partner_cleaned.is_set()
    assert unexpected == []


@pytest.mark.asyncio
async def test_caller_cancellation_drains_workers_without_starting_queued_jobs():
    started = []
    cleaned = []
    ready = asyncio.Event()

    async def blocked(index):
        started.append(index)
        if len(started) == 2:
            ready.set()
        try:
            await asyncio.Event().wait()
        finally:
            await asyncio.sleep(0)
            cleaned.append(index)

    running = asyncio.create_task(
        run_tasks_concurrently([partial(blocked, i) for i in range(4)], 2)
    )
    try:
        await asyncio.wait_for(ready.wait(), 2)
    finally:
        running.cancel()
        with pytest.raises(asyncio.CancelledError):
            await running
    assert started == [0, 1]
    assert sorted(cleaned) == [0, 1]


@pytest.mark.asyncio
async def test_empty_task_list_and_sequential_failure():
    assert await run_tasks_concurrently([], 3) == []
    called = []

    async def fail():
        raise ValueError("first task")

    async def queued():
        called.append(True)

    with pytest.raises(ValueError, match="first task"):
        await run_tasks_concurrently([fail, queued])
    assert called == []
