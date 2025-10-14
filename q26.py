"""Module for solving question 26 - Email pattern matching with regex."""

import re


def match_email(input_str):
    """
    Check if string matches valid email pattern.
    Input: "test@domain.com"
    Output: True

    Args:
        input_str (str): String to validate
    Returns:
        bool: Boolean indicating if string is valid email
    """
    # Basic validation checks
    if not input_str or "@" not in input_str:
        return False

    # Check for consecutive dots anywhere in the email
    if ".." in input_str:
        return False

    # Split into local and domain parts
    parts = input_str.split("@")
    if len(parts) != 2:
        return False

    local, domain = parts

    # Local part cannot be empty or start/end with dot
    if not local or local.startswith(".") or local.endswith("."):
        return False

    # Domain part cannot be empty or end with dot, must have at least one dot
    if not domain or domain.endswith(".") or "." not in domain:
        return False

    # Use regex for final validation
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, input_str))


# Test the function
result = match_email("test@domain.com")
print(f"Is valid email: {result}")
