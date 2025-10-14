"""Module docstring."""


def custom_filter(input_list):
    """
    function takes list as an input
    return a list of strings that starts with a
    """
    result = []
    for i in input_list:
        if i[0] == "a":
            result.append(i)

    return result


def test_custom_filter():
    """Test the custom_filter function."""
    test_list = ["apple", "banana", "avocado", "cherry", "apricot"]
    expected = ["apple", "avocado", "apricot"]
    result = custom_filter(test_list)
    print(f"Input: {test_list}")
    print(f"Filtered: {result}")
    print(f"Expected: {expected}")
    print(f"Test passed: {result == expected}")


if __name__ == "__main__":
    test_custom_filter()
