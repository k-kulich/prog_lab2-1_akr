import functools
import time


def retry(attempts=3, delay=1.0, exceptions=None):
    """Декоратор, который повторяет вызов функции при возникновении
    исключения из списка `exceptions` (или любого, если список None).

    :param attempts: общее число попыток (включая первую)
    :param delay: задержка между попытками в секундах
    :param exceptions: кортеж классов исключений или None
    """
    if attempts < 1:
        raise ValueError("attempts must be >= 1")
    if delay < 0:
        raise ValueError("delay must be >= 0")

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exc = None
            for attempt in range(1, attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as exc:
                    if exceptions is not None and not isinstance(exc, tuple(exceptions)):
                        raise
                    last_exc = exc
                    if attempt < attempts and delay > 0:
                        time.sleep(delay)
            raise last_exc

        return wrapper

    return decorator


if __name__ == '__main__':
    call_counter = {"n": 0}

    @retry(attempts=3, delay=0.1, exceptions=(ValueError,))
    def flaky():
        call_counter["n"] += 1
        if call_counter["n"] < 3:
            raise ValueError(f"fail #{call_counter['n']}")
        return "ok"

    print(flaky())