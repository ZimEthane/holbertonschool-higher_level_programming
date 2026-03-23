import logging

# Configure logging
logging.basicConfig(level=logging.ERROR, format='%(levelname)s: %(message)s')


def generate_invitations(template, attendees):
    """
    Generate personalized invitation files from a template.

    Parameters:
    template (str): String template with placeholders
    attendees (list): List of dictionaries containing attendee data
    """

    # Check input types - template must be a string
    if not isinstance(template, str):
        logging.error(f"Invalid input type for template: {type(template).__name__}. Expected str.")
        return

    # Check input types - attendees must be a list
    if not isinstance(attendees, list):
        logging.error(f"Invalid input type for attendees: {type(attendees).__name__}. Expected list.")
        return

    # Check if attendees is a list of dictionaries
    if attendees and not all(isinstance(item, dict) for item in attendees):
        logging.error("Invalid input: attendees must be a list of dictionaries.")
        return

    # Check if template is empty
    if not template or not template.strip():
        logging.error("Template is empty, no output files generated.")
        return

    # Check if attendees list is empty
    if not attendees:
        logging.error("No data provided, no output files generated.")
        return

    # Define placeholders
    placeholders = ["name", "event_title", "event_date", "event_location"]

    # Process each attendee
    for index, attendee in enumerate(attendees, start=1):
        output_content = template

        # Replace placeholders
        for placeholder in placeholders:
            value = attendee.get(placeholder, "N/A")
            # Handle None values
            if value is None:
                value = "N/A"
            output_content = output_content.replace(f"{{{placeholder}}}", str(value))

        # Write to output file
        output_filename = f"output_{index}.txt"
        try:
            with open(output_filename, 'w') as file:
                file.write(output_content)
        except IOError as e:
            logging.error(f"Error writing to {output_filename}: {e}")
