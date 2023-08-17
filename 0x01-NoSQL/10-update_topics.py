#!/usr/bin/env python3
"""
Module demostrates basic MongoDB manipulation with pymongo
"""


def update_topics(mongo_collection, name, topics):
    """
    function changes all topics of a school document based on the name
    """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
