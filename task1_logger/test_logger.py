import io
import unittest
from contextlib import redirect_stdout

from logger import logger


class TestLoggerDecorator(unittest.TestCase):
    def test_logs_function_name_args_and_result(self):
        @logger
        def add(a, b):
            return a + b

        buf = io.StringIO()
        with redirect_stdout(buf):
            result = add(2, 3)

        self.assertEqual(result, 5)
        output = buf.getvalue()
        self.assertIn("add", output)
        self.assertIn("args=(2, 3)", output)
        self.assertIn("result=5", output)
        self.assertIn("time=", output)

    def test_logs_kwargs(self):
        @logger
        def greet(name, greeting="Hello"):
            return f"{greeting}, {name}!"

        buf = io.StringIO()
        with redirect_stdout(buf):
            greet("Bob", greeting="Hi")

        output = buf.getvalue()
        self.assertIn("kwargs={'greeting': 'Hi'}", output)
        self.assertIn("result='Hi, Bob!'", output)

    def test_preserves_metadata(self):
        @logger
        def sample():
            """Docstring of sample."""
            return 1

        self.assertEqual(sample.__name__, "sample")
        self.assertEqual(sample.__doc__, "Docstring of sample.")

    def test_logs_exception(self):
        @logger
        def failing():
            raise ValueError("boom")

        buf = io.StringIO()
        with redirect_stdout(buf):
            with self.assertRaises(ValueError):
                failing()

        output = buf.getvalue()
        self.assertIn("raised=ValueError('boom')", output)


if __name__ == '__main__':
    unittest.main()