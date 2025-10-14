"""Module docstring."""


def square_greate_than_three(input_list):
    """
    takes list as an input
    return a list of squares of no greater than 3
    """
    total = []
    for i in input_list:
        if i > 3:
            total.append(i * i)
        else:
            continue

    return total


def test_square_greate_than_three():
    """Test the square_greate_than_three function."""
    test_list = [1, 2, 3, 4, 5, 6]
    expected = [16, 25, 36]
    result = square_greate_than_three(test_list)
    print(f"Input: {test_list}")
    print(f"Squares > 3: {result}")
    print(f"Expected: {expected}")
    print(f"Test passed: {result == expected}")


if __name__ == "__main__":
    test_square_greate_than_three()
