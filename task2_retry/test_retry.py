import unittest

from retry import retry


class TestRetryDecorator(unittest.TestCase):
    def test_no_retry_when_success(self):
        calls = {"n": 0}

        @retry(attempts=3, delay=0)
        def ok():
            calls["n"] += 1
            return "done"

        self.assertEqual(ok(), "done")
        self.assertEqual(calls["n"], 1)

    def test_retry_until_success(self):
        calls = {"n": 0}

        @retry(attempts=5, delay=0)
        def flaky():
            calls["n"] += 1
            if calls["n"] < 3:
                raise ValueError("nope")
            return "ok"

        self.assertEqual(flaky(), "ok")
        self.assertEqual(calls["n"], 3)

    def test_all_attempts_fail(self):
        calls = {"n": 0}

        @retry(attempts=3, delay=0)
        def always_fail():
            calls["n"] += 1
            raise RuntimeError("boom")

        with self.assertRaises(RuntimeError):
            always_fail()
        self.assertEqual(calls["n"], 3)

    def test_exception_filter_passes_through(self):
        calls = {"n": 0}

        @retry(attempts=3, delay=0, exceptions=(ValueError,))
        def raises_other():
            calls["n"] += 1
            raise KeyError("not retryable")

        with self.assertRaises(KeyError):
            raises_other()
        self.assertEqual(calls["n"], 1)

    def test_invalid_arguments(self):
        with self.assertRaises(ValueError):
            retry(attempts=0)
        with self.assertRaises(ValueError):
            retry(attempts=1, delay=-1)

    def test_delay_between_attempts(self):
        import time
        calls = {"n": 0}

        @retry(attempts=3, delay=0.05)
        def flaky():
            calls["n"] += 1
            if calls["n"] < 3:
                raise ValueError("retry")
            return "ok"

        start = time.perf_counter()
        flaky()
        elapsed = time.perf_counter() - start
        self.assertGreaterEqual(elapsed, 0.1)


if __name__ == '__main__':
    unittest.main()