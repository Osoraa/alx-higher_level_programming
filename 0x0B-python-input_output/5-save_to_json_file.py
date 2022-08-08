#!/usr/bin/python3
"""Save to JSON file module."""

import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a file in JSON format.

    Args:
        my_obj: Python object to write to <filename>.
        filename: JSON representation file destination.

    Returns:
        Nothing.
    """

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
