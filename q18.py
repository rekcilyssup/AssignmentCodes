"""Module for solving question 18 - Distance from zero function."""


def type_checking(some_input):
    """
    Return absolute value if input is int/float, else return "Nope".
    Input: 12.30 -> Output: 12.3
    Input: "string" -> Output: "Nope"

    Args:
        some_input (any): Input to check and convert
    Returns:
        float or str: Absolute value or "Nope"
    """
    if isinstance(some_input, (int, float)):
        return abs(some_input)
    return "Nope"


# Test the function
result1 = type_checking(12.30)
result2 = type_checking("string")
print(f"Test 1: {result1}")
print(f"Test 2: {result2}")
