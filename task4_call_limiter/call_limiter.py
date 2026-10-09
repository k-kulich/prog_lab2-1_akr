import functools


def _is_magic(name: str) -> bool:
    return name.startswith('__') and name.endswith('__')


def _limit_wrap(func, limit, method_name):
    counter = {"calls": 0}

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if counter["calls"] >= limit:
            raise RuntimeError(
                f"Method '{method_name}' call limit ({limit}) exceeded"
            )
        counter["calls"] += 1
        return func(*args, **kwargs)

    return wrapper


def call_limiter(limit):
    """Декоратор класса, ограничивающий число вызовов каждого
    публичного метода значением `limit`.

    Магические методы (dunder) не ограничиваются, чтобы не ломать
    стандартное поведение объектов (создание, сравнение, repr и т.п.).
    """
    if limit < 0:
        raise ValueError("limit must be >= 0")

    def decorate(klass):
        for name, attr in list(vars(klass).items()):
            if _is_magic(name):
                continue
            if isinstance(attr, staticmethod):
                setattr(klass, name, staticmethod(_limit_wrap(attr.__func__, limit, name)))
            elif isinstance(attr, classmethod):
                setattr(klass, name, classmethod(_limit_wrap(attr.__func__, limit, name)))
            elif callable(attr):
                setattr(klass, name, _limit_wrap(attr, limit, name))
        return klass

    return decorate


if __name__ == '__main__':
    @call_limiter(limit=2)
    class Service:
        def ping(self):
            return "pong"

    s = Service()
    print(s.ping())
    print(s.ping())
    try:
        s.ping()
    except RuntimeError as e:
        print(f"Error: {e}")