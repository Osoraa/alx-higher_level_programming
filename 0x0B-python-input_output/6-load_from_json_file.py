#!/usr/bin/python3
"""Load from JSON file module."""

import json


def load_from_json_file(filename):
    """Converts json object in a file to an Python object.

    Args:
        filename: File containing valid JSON string format.

    Returns:
        Corresponding Python object.
    """

    with open(filename, "r", encoding="utf-8") as file:
        return (json.load(file))
