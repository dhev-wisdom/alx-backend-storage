#!/usr/bin/env python3
"""
Module obtain the HTML content of a particular URL and returns it.
"""

import redis
import requests


def get_page(url: str) -> str:
    """
    function  obtain the HTML content of a particular URL and returns it.
    """
    response = requests.get(url)
    content = response.text

    r = redis.Redis()
    count_key = f"count:{url}"
    r.incr(count_key)

    cache_key = f"cache:{url}"
    r.setex(cache_key, 10, content)

    return content
