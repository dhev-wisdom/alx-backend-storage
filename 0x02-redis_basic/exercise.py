#!/usr/bin/env python3
"""
Introduction to Redis database
"""

import redis
import uuid
from typing import Union


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
