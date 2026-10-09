import io
import unittest
from contextlib import redirect_stdout

from async_demo import task_first, task_second


class TestAsyncDemo(unittest.IsolatedAsyncioTestCase):
    async def test_task_first_prints_three_lines(self):
        buf = io.StringIO()
        with redirect_stdout(buf):
            await task_first(sleep_a=0, sleep_b=0)

        lines = [l for l in buf.getvalue().splitlines() if l.strip()]
        self.assertEqual(
            lines,
            ["Task 1: step 1", "Task 1: step 2", "Task 1: step 3"],
        )

    async def test_task_second_prints_four_lines(self):
        buf = io.StringIO()
        with redirect_stdout(buf):
            await task_second(sleep_a=0, sleep_b=0, sleep_c=0)

        lines = [l for l in buf.getvalue().splitlines() if l.strip()]
        self.assertEqual(
            lines,
            [
                "Task 2: step 1",
                "Task 2: step 2",
                "Task 2: step 3",
                "Task 2: step 4",
            ],
        )

    async def test_runs_concurrently(self):
        import asyncio
        import time

        start = time.perf_counter()
        await asyncio.gather(
            task_first(sleep_a=0.1, sleep_b=0.2),
            task_second(sleep_a=0.15, sleep_b=0.05, sleep_c=0.05),
        )
        elapsed = time.perf_counter() - start
        self.assertLess(elapsed, 0.5)


if __name__ == '__main__':
    unittest.main()