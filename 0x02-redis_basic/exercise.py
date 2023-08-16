#!/usr/bin/env python3
"""
Introduction to Redis database
"""

import redis
import uuid
from typing import Callable, Union


class Cache():
    """
    Cache class in the __init__ method of redis
    """

    def __init__(self):
        """
        init method
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        store method
        """
        random_key = str(uuid.uuid4())
        self._redis.set(random_key, data)
        return random_key

    def get(self, key: str, fn: Callable = None) -> Union[str, bytes, int, float]:
        """
        custom get method
        """
        value = self._redis.get(key)
        if value is None:
            return None
        if fn is None:
            return None
        return fn(value)

    def get_str(self, key: str) -> str:
        """
        get_str method
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """
        get_int method
        """
        return self.get(key, fn=int)
