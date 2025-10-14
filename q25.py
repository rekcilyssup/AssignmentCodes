"""Module docstring."""

from datetime import datetime


def find_absolute_diff(input_list):
    """
    Accepts an list as a parameter
    returns output

    """

    # Write your code
    date_format = "%a %d %b %Y %H:%M:%S %z"
    time1 = datetime.strptime(input_list[0], date_format)
    time2 = datetime.strptime(input_list[1], date_format)
    diff = abs((time1 - time2).total_seconds())
    return diff


def test_find_absolute_diff():
    """Test the find_absolute_diff function."""
    test_timestamps = [
        "Sat 02 May 2015 19:54:36 +0530",
        "Fri 01 May 2015 13:54:36 -0000",
    ]
    result = find_absolute_diff(test_timestamps)
    print(f"Input: {test_timestamps}")
    print(f"Absolute difference in seconds: {result}")


if __name__ == "__main__":
    test_find_absolute_diff()
