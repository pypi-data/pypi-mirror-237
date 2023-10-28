import uuid
from datetime import datetime


def is_valid_date(text: str) -> bool:
    """
    Check if the given text represents a valid date in the format YYYY-MM-DD.

    Parameters:
        text (str): The text to be checked.

    Returns:
        bool: True if the text represents a valid date, False otherwise.
    """
    try:
        datetime.strptime(text, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def is_uuid(text: str) -> bool:
    """
    Check if a string is a valid UUID.

    Args:
        text (str): The string to check.

    Returns:
        bool: True if the string is a valid UUID, False otherwise.
    """
    try:
        uuid.UUID(text)
        return True
    except ValueError:
        return False
