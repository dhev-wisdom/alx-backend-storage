#!/usr/bin/env python3
"""
Module returns all students sorted by average score
"""


def top_students(mongo_collection):
    """
    Function returns all students sorted by average score
    """
    average_score = [
            {"$unwind": "$topics"},
            {"$group": {"_id": "$name",
             "averageScore": {"$avg": "$topics.score"}}},
            {"$sort": {"averageScore", -1}}
        ]
    collections = mongo_collection.aggregate(average_score)
    return list(collection)
