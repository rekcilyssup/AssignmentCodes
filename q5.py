"""Module docstring."""



def sort_asc(input_dict):
    """
    Sort dictionary by key and value.
    Input: {"ravi": 10, "rajnish": 9, "sanjeev": 15, "yash": 2, "suraj": 32}
    Output: {"key": {"rajnish": "9", "ravi": "10"...}, "value": {"yash": 2...}}

    Args:
        input_dict (dict): Dictionary to sort
    Returns:
        dict: Dictionary with key and value sorted versions
    """
    sorted_by_key = {}
    for key in sorted(input_dict.keys()):
        sorted_by_key[key] = str(input_dict[key])
    sorted_by_value = {}
    for key, val in sorted(input_dict.items(), key=lambda x: x[1]):
        sorted_by_value[key] = val
    return {"key": sorted_by_key, "value": sorted_by_value}


# Test the function
test_dict = {"ravi": 10, "rajnish": 9, "sanjeev": 15, "yash": 2, "suraj": 32}
result = sort_asc(test_dict)
print(f"Sorted dictionary: {result}")
