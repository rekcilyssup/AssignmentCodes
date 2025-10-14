"""Module f    Args:
        input_str (str): Date string in format \"DD MM YYYY\"
    Returns:
        str: Day of week in uppercaseolving question 24 - Find day of week for given date."""

from datetime import datetime


def find_day(input_str):
    """
    Find day of week for given date.
    Input: "08 05 2015"
    Output: "FRIDAY"

    Args:
        input_str (str): Date string in format "DD MM YYYY"
    Returns:
        str: Day of week in uppercase
    """
    date_obj = datetime.strptime(input_str, "%d %m %Y")
    day = date_obj.strftime("%A").upper()
    return day


# Test the function
result = find_day("08 05 2015")
print(f"Day of week: {result}")
