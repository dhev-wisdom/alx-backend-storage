#!/usr/bin/env python3
"""
Module demostrate how to use mongodb with python
"""


def list_all(mongo_collection):
    """
    function lists all documents in a mongodb collection
    """
    cur = mongo_collection.find({})
    document_list = list(cur)

    return document_list
