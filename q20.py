"""Module for solving question 20 - Custom map implementation."""


def custom_map(input_list):
    """
    Custom map function - check if strings start with 'a'.
    Input: ["apple", "banana", "pear", "apricot", "orange"]
    Output: [True, False, False, True, False]

    Args:
        input_list (list): List of strings
    Returns:
        list: List of booleans indicating if each string starts with 'a'
    """
    mapped_result = []
    for item in input_list:
        if item[0] == "a":
            mapped_result.append(True)
        else:
            mapped_result.append(False)
    return mapped_result


# Test the function
test_list = ["apple", "banana", "pear", "apricot", "orange"]
RESULT = custom_map(test_list)
print(f"Map result: {RESULT}")
