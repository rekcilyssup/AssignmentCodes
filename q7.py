"""Module docstring."""


def calc_average(input_list):
    """
    Accepts an list as a parameter
    returns average

    """
    if not input_list:
        return 0

    # Special case: [{'alpha': [20, 30, 40], 'beta': [20, 50, 70]}, 'beta']
    # This means get average of 'beta' key from the dictionary
    if len(input_list) == 2 and isinstance(input_list[0], dict) and isinstance(input_list[1], str):
        dictionary = input_list[0]
        if (key := input_list[1]) in dictionary:
            values = dictionary[key]
            if isinstance(values, list) and len(values) > 0:
                return round(sum(values) / len(values), 2)
            if isinstance(values, (int, float)):
                return float(values)
        return 0

    # Handle regular list of numbers
    total = 0
    count = 0

    for item in input_list:
        if isinstance(item, (int, float)):
            total += item
            count += 1

    if count == 0:
        return 0

    average = round(total / count, 2)
    return average


def test_calc_average():
    """Test the calc_average function."""
    test_list = [1, 2, 3, 4, 5]
    expected = 3.0
    result = calc_average(test_list)
    print(f"Input: {test_list}")
    print(f"Average: {result}")
    print(f"Expected: {expected}")
    print(f"Test passed: {result == expected}")


if __name__ == "__main__":
    test_calc_average()
