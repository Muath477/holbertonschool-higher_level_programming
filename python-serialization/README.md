# Python – Serialization

This project covers serializing and deserializing Python data: JSON, pickle,
CSV-to-JSON conversion, and XML.

## Files

| File | Description |
| --- | --- |
| `task_00_basic_serialization.py` | `serialize_and_save_to_file(data, filename)` saves a dictionary as JSON; `load_and_deserialize(filename)` reads it back. |
| `task_01_pickle.py` | `CustomObject` with `display()`, `serialize(filename)` and the class method `deserialize(filename)` using `pickle`. Returns `None` for missing or malformed files. |
| `task_02_csv.py` | `convert_csv_to_json(csv_filename)` converts a CSV file to `data.json` with `csv.DictReader`. Returns `False` if the file cannot be read. |
| `task_03_xml.py` | `serialize_to_xml(dictionary, filename)` and `deserialize_from_xml(filename)` using `xml.etree.ElementTree`. |

## Requirements

- Ubuntu 20.04 LTS, Python 3.8
- Code style checked with `pycodestyle`
- Every file starts with `#!/usr/bin/env python3` and ends with a newline
- Every module, class and function is documented
