#!/usr/bin/python3
"""
Module demostrate how to use mongodb with python
"""


def list_all(mongo_collection):
    """
    function lists all documents in a mongodb collection
    """
    collections = mongo_collection.find({})
    col_list = list(collections)
    return col_list
