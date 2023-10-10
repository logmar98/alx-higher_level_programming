#!/usr/bin/python3
"""Python class-to-JSON function"""


def class_to_json(obj):
    """dictionary represntation of simple data structure"""
    return obj.__dict__
