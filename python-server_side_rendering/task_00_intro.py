#!/usr/bin/python3
"""Fill an invitation template once per attendee and save each result."""

PLACEHOLDERS = ["name", "event_title", "event_date", "event_location"]


def generate_invitations(template, attendees):
    """Write output_1.txt, output_2.txt, ... from template and attendees.

    Every {placeholder} is replaced by the attendee's value, or "N/A" when
    the value is missing or None. Nothing is written if the input is wrong.
    """
    if not isinstance(template, str):
        print("Invalid input: template must be a string, got {}"
              .format(type(template).__name__))
        return
    if not isinstance(attendees, list) or \
            not all(isinstance(person, dict) for person in attendees):
        print("Invalid input: attendees must be a list of dictionaries")
        return

    if not template.strip():
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return

    for index, person in enumerate(attendees, start=1):
        invitation = template
        for key in PLACEHOLDERS:
            value = person.get(key)
            if value is None or value == "":
                value = "N/A"
            invitation = invitation.replace("{" + key + "}", str(value))

        filename = "output_{}.txt".format(index)
        try:
            with open(filename, "w", encoding="utf-8") as output:
                output.write(invitation)
        except OSError as error:
            print("Could not write {}: {}".format(filename, error))
