#!/usr/bin/env python3
"""
Module demostrates basics of using pymongo with python
"""


def insert_school(mongo_collection, **kwargs):
    """
    function documentation
    """
    inserted_documents = mongo_collection.insert_many([doc for doc in kwargs.values()])

    return inserted_documents.inserted_ids
