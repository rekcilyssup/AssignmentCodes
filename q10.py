"""Module for solving question 10 - Split and join string with hyphens."""


def join_string(input_str):
    """
    Split string by spaces and join with hyphens.
    Input: "this is a string"
    Output: "this-is-a-string"

    Args:
        input_str (str): String to modify
    Returns:
        str: String with spaces replaced by hyphens
    """
    return input_str.replace(" ", "-")


# Test the function
RESULT = join_string("this is a string")
print(f"Joined string: {RESULT}")
