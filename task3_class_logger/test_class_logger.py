import io
import unittest
from contextlib import redirect_stdout

from class_logger import logger


class TestClassLogger(unittest.TestCase):
    def test_regular_methods_logged(self):
        @logger
        class Calc:
            def add(self, a, b):
                return a + b

        buf = io.StringIO()
        with redirect_stdout(buf):
            Calc().add(2, 3)

        output = buf.getvalue()
        self.assertIn("Calc.add", output)
        self.assertIn("result=5", output)

    def test_magic_methods_logged_by_default(self):
        @logger
        class Magic:
            def __init__(self, v):
                self.v = v

            def __len__(self):
                return self.v

        buf = io.StringIO()
        with redirect_stdout(buf):
            len(Magic(7))

        output = buf.getvalue()
        self.assertIn("Magic.__init__", output)
        self.assertIn("Magic.__len__", output)

    def test_magic_methods_disabled(self):
        @logger(show_magic_methods=False)
        class Quiet:
            def __init__(self, v):
                self.v = v

            def __len__(self):
                return self.v

            def plain(self):
                return "ok"

        buf = io.StringIO()
        with redirect_stdout(buf):
            q = Quiet(5)
            q.plain()
            len(q)

        output = buf.getvalue()
        self.assertNotIn("Quiet.__init__", output)
        self.assertNotIn("Quiet.__len__", output)
        self.assertIn("Quiet.plain", output)

    def test_static_and_class_methods(self):
        @logger
        class Util:
            @staticmethod
            def sm(a):
                return a + 1

            @classmethod
            def cm(cls, a):
                return a + 2

        buf = io.StringIO()
        with redirect_stdout(buf):
            Util.sm(1)
            Util.cm(1)

        output = buf.getvalue()
        self.assertIn("Util.sm", output)
        self.assertIn("Util.cm", output)


if __name__ == '__main__':
    unittest.main()