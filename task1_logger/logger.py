import functools
import time


def logger(func):
    """Декоратор, который логирует имя функции, ее аргументы, результат и время выполнения."""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        try:
            result = func(*args, **kwargs)
        except Exception as exc:
            elapsed = time.perf_counter() - start
            print(
                f"[LOG] {func.__qualname__} "
                f"args={args} kwargs={kwargs} "
                f"raised={exc!r} time={elapsed:.6f}s"
            )
            raise
        elapsed = time.perf_counter() - start
        print(
            f"[LOG] {func.__qualname__} "
            f"args={args} kwargs={kwargs} "
            f"result={result!r} time={elapsed:.6f}s"
        )
        return result

    return wrapper


if __name__ == '__main__':
    @logger
    def add(a, b):
        return a + b

    @logger
    def greet(name, greeting="Hello"):
        return f"{greeting}, {name}!"

    add(2, 3)
    greet("Alice")
    greet("Bob", greeting="Hi")