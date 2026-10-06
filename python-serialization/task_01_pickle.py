#!/usr/bin/env python3
"""Define a CustomObject class that can be pickled to and from a file."""
import pickle


class CustomObject:
    """Represent a person with a name, an age and a student status."""

    def __init__(self, name, age, is_student):
        """Initialize a new CustomObject.

        Args:
            name (str): The name of the person.
            age (int): The age of the person.
            is_student (bool): Whether the person is a student.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print the attributes of the object."""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """Pickle the current instance and save it to a file.

        Args:
            filename (str): The name of the output file.
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except OSError:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Load a pickled CustomObject from a file.

        Args:
            filename (str): The name of the file to load.

        Returns:
            CustomObject: The loaded instance, or None if the file does not
            exist or is malformed.
        """
        try:
            with open(filename, "rb") as f:
                obj = pickle.load(f)
        except (OSError, pickle.UnpicklingError, EOFError, AttributeError,
                ImportError, IndexError, TypeError, ValueError):
            return None
        if not isinstance(obj, cls):
            return None
        return obj
