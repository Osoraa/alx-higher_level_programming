#!/usr/bin/python3
"""To JSON String module."""

import json


def to_json_string(my_obj):
    """Represents an object in JSON format.

    Args:
        my_obj: Object to parse to JSON representation.

    Returns:
        JSON representation of an object.
    """

    return json.dumps(my_obj)
