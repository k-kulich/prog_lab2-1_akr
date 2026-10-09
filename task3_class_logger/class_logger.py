import functools
import time


def _wrap_method(func, class_name):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        try:
            result = func(*args, **kwargs)
        except Exception as exc:
            elapsed = time.perf_counter() - start
            print(
                f"[CLASS LOG] {class_name}.{func.__name__} "
                f"args={args} kwargs={kwargs} "
                f"raised={exc!r} time={elapsed:.6f}s"
            )
            raise
        elapsed = time.perf_counter() - start
        print(
            f"[CLASS LOG] {class_name}.{func.__name__} "
            f"args={args} kwargs={kwargs} "
            f"result={result!r} time={elapsed:.6f}s"
        )
        return result

    return wrapper


def _is_magic(name: str) -> bool:
    return name.startswith('__') and name.endswith('__')


def logger(cls=None, *, show_magic_methods: bool = True):
    """Декоратор класса: логирует вызовы всех методов (включая магические).
    Поддерживает оба варианта использования:
        @logger
        class A: ...
        @logger(show_magic_methods=False)
        class B: ...
    """

    def decorate(klass):
        for name, attr in list(vars(klass).items()):
            if _is_magic(name) and not show_magic_methods:
                continue
            if isinstance(attr, staticmethod):
                setattr(klass, name, staticmethod(_wrap_method(attr.__func__, klass.__name__)))
            elif isinstance(attr, classmethod):
                setattr(klass, name, classmethod(_wrap_method(attr.__func__, klass.__name__)))
            elif callable(attr):
                setattr(klass, name, _wrap_method(attr, klass.__name__))
        return klass

    if cls is None:
        return decorate
    return decorate(cls)


if __name__ == '__main__':
    @logger
    class Calc:
        def __init__(self, base):
            self.base = base

        def add(self, x):
            return self.base + x

        def __str__(self):
            return f"Calc({self.base})"

    c = Calc(10)
    print(c.add(5))
    print(str(c))

    print("--- без магических методов ---")

    @logger(show_magic_methods=False)
    class Quiet:
        def __init__(self, x):
            self.x = x

        def double(self):
            return self.x * 2

        def __repr__(self):
            return f"Quiet({self.x})"

    q = Quiet(4)
    print(q.double())