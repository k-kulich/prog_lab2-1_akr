import unittest

from call_limiter import call_limiter


class TestCallLimiter(unittest.TestCase):
    def test_allows_up_to_limit(self):
        @call_limiter(limit=3)
        class A:
            def ping(self):
                return "pong"

        a = A()
        for _ in range(3):
            self.assertEqual(a.ping(), "pong")

    def test_exceeding_limit_raises(self):
        @call_limiter(limit=2)
        class A:
            def ping(self):
                return "pong"

        a = A()
        a.ping()
        a.ping()
        with self.assertRaises(RuntimeError):
            a.ping()

    def test_counters_are_independent_per_method(self):
        @call_limiter(limit=1)
        class A:
            def first(self):
                return 1

            def second(self):
                return 2

        a = A()
        self.assertEqual(a.first(), 1)
        self.assertEqual(a.second(), 2)
        with self.assertRaises(RuntimeError):
            a.first()
        with self.assertRaises(RuntimeError):
            a.second()

    def test_static_and_class_methods(self):
        @call_limiter(limit=1)
        class A:
            @staticmethod
            def s():
                return "s"

            @classmethod
            def c(cls):
                return "c"

        A.s()
        A.c()
        with self.assertRaises(RuntimeError):
            A.s()
        with self.assertRaises(RuntimeError):
            A.c()

    def test_invalid_limit(self):
        with self.assertRaises(ValueError):
            call_limiter(-1)


if __name__ == '__main__':
    unittest.main()