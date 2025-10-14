"""Module docstring."""


def is_palindrome(input_str):
    """
    Check if a string is palindrome.
    Input: "aba"
    Output: True

    Args:
        input_str (str): String to check
    Returns:
        bool: Boolean indicating if string is palindrome
    """
    return input_str == input_str[::-1]


# Test the function
RESULT = is_palindrome("aba")
print(f"Is palindrome: {RESULT}")
