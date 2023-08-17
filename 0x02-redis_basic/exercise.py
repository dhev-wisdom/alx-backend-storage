#!/usr/bin/env python3
"""
Introduction to Redis database
"""

from functools import wraps
import redis
import uuid
from typing import Callable, Union, Optional


def replay(method: Callable) -> Callable:
    """
    function displays history of calls of a particular function
    """
    key = method.__qualname__
    inputs = f"{key}:inputs"
    outputs = f"{key}:outputs"
    redis = method.__self__.redis
    count = redis.get(key).decode("utf-8")
    print(f"{key} was called {count} times")
    inputList = redis.lrange(inputs, 0, -1)
    outputList = redis.lrange(outputs, 0, -1)
    zipped_redis = list(zip(inputList, outputList))
    for i, j in zipped_redis:
        attr = i.decode("utf-8")
        data = j.decode("utf-8")
        print(f"{key}(*{attr}) -> {data}")


def call_history(method: Callable) -> Callable:
    """
    call_history decorator to store the history of inputs and outputs
    for a particular function
    """
    key = method.__qualname__
    inputs = f"{key}:inputs"
    outputs = f"{key}:outputs"

    @wraps(method)
    def wrapper(self, *arg, **kwarg):
        self._redis.rpush(inputs, str(arg))
        data = method(self, *arg, **kwarg)
        self._redis.rpush(outputs, str(data))
        return data
    return wrapper


def count_calls(method: Callable) -> Callable:
    """
    count_calls static method
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *arg, **kwarg):
        self._redis.incr(key)
        return method(self, *arg, **kwarg)
    return wrapper


class Cache(object):
    """
    Cache class in the __init__ method of redis
    """

    def __init__(self):
        """
        init method
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        store method
        """
        random_key = str(uuid.uuid4())
        self._redis.set(random_key, data)
        return random_key

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """
        custom get method
        """
        value = self._redis.get(key)
        if fn:
            return fn(value)
        return value

    def get_str(self, key: str) -> str:
        """
        get_str method
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """
        get_int method
        """
        data = self._redis.get(key)
        try:
            data = int(value.decode("utf-8"))
        except Exception:
            data = 0
        return data
