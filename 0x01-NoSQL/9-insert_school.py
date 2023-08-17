#!/usr/bin/env python3
"""
Module demostrates basics of using pymongo with python
"""


def insert_school(mongo_collection, **kwargs):
    """
    function documentation
    """
    inserted_document = mongo_collection.insert_one(kwargs)

    return inserted_document.inserted_id
