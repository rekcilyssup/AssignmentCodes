"""Module d    length = len(input_list)
    for i in range(length):
        for j in range(0, length-i-1):tring."""


def sort_by_second_value(input_list):
    """
    Accepts an list as a parameter
    returns sorted list

    """

    # Write your code
    length = len(input_list)
    for i in range(length):
        for j in range(0, length - i - 1):
            if input_list[j][1] > input_list[j + 1][1]:
                temp = input_list[j]
                input_list[j] = input_list[j + 1]
                input_list[j + 1] = temp

    return input_list


def test_sort_by_second_value():
    """Test the sort_by_second_value function."""
    test_list = [(1, 3), (3, 2), (2, 1)]
    expected = [(2, 1), (3, 2), (1, 3)]
    result = sort_by_second_value(test_list)
    print(f"Input: {test_list}")
    print(f"Sorted: {result}")
    print(f"Expected: {expected}")
    print(f"Test passed: {result == expected}")


if __name__ == "__main__":
    test_sort_by_second_value()
