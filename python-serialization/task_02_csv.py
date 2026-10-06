#!/usr/bin/env python3
"""Convert a CSV file to JSON and save it to data.json."""
import csv
import json


def convert_csv_to_json(csv_filename):
    """Read a CSV file and write its rows to data.json as a JSON list.

    Args:
        csv_filename (str): The name of the CSV file to convert.

    Returns:
        bool: True if the conversion succeeded, False otherwise.
    """
    try:
        with open(csv_filename, "r", encoding="utf-8", newline="") as csv_file:
            rows = list(csv.DictReader(csv_file))
        with open("data.json", "w", encoding="utf-8") as json_file:
            json.dump(rows, json_file)
    except (OSError, csv.Error):
        return False
    return True
