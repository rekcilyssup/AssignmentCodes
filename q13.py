"""Module for solving question 13 - Count character types in string."""


def count_up_lo_di_sym(input_str):
    """
    Count lowercase, uppercase, digits, and special symbols.
    Input: "P@#yn26at^&i5ve"
    Output: {"lowercase": 7, "uppercase": 1, "digit": 3, "symbol": 4}

    Args:
        input_str (str): String to analyze
    Returns:
        dict: Dictionary with character type counts
    """
    counts = {"lowercase": 0, "uppercase": 0, "digit": 0, "symbol": 0}
    for char in input_str:
        if char.isupper():
            counts["uppercase"] += 1
        elif char.islower():
            counts["lowercase"] += 1
        elif char.isdigit():
            counts["digit"] += 1
        else:
            counts["symbol"] += 1
    return counts


# Test the function
RESULT = count_up_lo_di_sym("P@#yn26at^&i5ve")
print(f"Character counts: {RESULT}")
