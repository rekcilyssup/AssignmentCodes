"""Module docstring."""


def custom_reducer(input_list):
    """
    takes list as an input
    return the summation of the values
    """
    total = 0
    for i in input_list:
        total += i

    return total


def test_custom_reducer():
    """Test the custom_reducer function."""
    test_list = [1, 2, 3, 4, 5]
    expected = 15
    result = custom_reducer(test_list)
    print(f"Input: {test_list}")
    print(f"Sum: {result}")
    print(f"Expected: {expected}")
    print(f"Test passed: {result == expected}")


if __name__ == "__main__":
    test_custom_reducer()
