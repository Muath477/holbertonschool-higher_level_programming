#!/usr/bin/env python3
"""Serialize a dictionary to a JSON file and deserialize it back."""
import json


def serialize_and_save_to_file(data, filename):
    """Serialize a dictionary to JSON and save it to a file.

    The file is replaced if it already exists.

    Args:
        data (dict): The dictionary to serialize.
        filename (str): The name of the output JSON file.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """Load a JSON file and recreate the Python object it contains.

    Args:
        filename (str): The name of the input JSON file.

    Returns:
        dict: The deserialized data.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
