#!/usr/bin/env python3
"""
Module documentation
"""


def schools_by_topic(mongo_collection, topic):
    """
    function returns the list of school having a specific topic:
    """
    cur = mongo_collection.find({"topics": topic})
    return list(cur)
