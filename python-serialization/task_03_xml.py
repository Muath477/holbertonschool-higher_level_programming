#!/usr/bin/env python3
"""Serialize a dictionary to XML and deserialize it back."""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize a dictionary to an XML file.

    Each key becomes a child element of <data> and each value its text.
    Values are stored as strings, since XML has no types.

    Args:
        dictionary (dict): The dictionary to serialize.
        filename (str): The name of the output XML file.
    """
    root = ET.Element("data")
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
    # ET.indent() needs Python 3.9+, so add the indentation by hand
    if len(root):
        root.text = "\n    "
        for child in root:
            child.tail = "\n    "
        root[-1].tail = "\n"
    ET.ElementTree(root).write(filename, encoding="utf-8")


def deserialize_from_xml(filename):
    """Read an XML file written by serialize_to_xml.

    Args:
        filename (str): The name of the XML file to read.

    Returns:
        dict: The dictionary with string values.
    """
    root = ET.parse(filename).getroot()
    return {child.tag: child.text or "" for child in root}
