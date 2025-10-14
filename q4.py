"""Module for solving question 4 - Replace first char occurrences with '$'."""


def modify_string(input_string):
    """
    Replace occurrences of first character with '$'.
    Input: "restart"
    Output: "re$ta$t"

    Args:
        input_string (str): String to modify
    Returns:
        str: Modified string
    """
    if not input_string:
        return ""
    first_char = input_string[0]
    new_string = input_string[1:].replace(first_char, "$")
    return first_char + new_string


# Test the function
RESULT = modify_string("restart")
print(f"Modified string: {RESULT}")
