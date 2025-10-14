"""Module for solving question 3 - Get three largest numbers from a list."""


def largest_number(numbers_list):
    """
    Get the three largest numbers from a list in one loop.
    Input: [23,5,8,14,63,12,45]
    Output: (63,45,23)

    Args:
        numbers_list (list): List of numbers
    Returns:
        tuple: Tuple of (first_largest, second_largest, third_largest)
    """
    first = second = third = float("-inf")
    for number in numbers_list:
        if number > first:
            third = second
            second = first
            first = number
        elif number > second:
            third = second
            second = number
        elif number > third:
            third = number
    return first, second, third


# Test the function
if __name__ == "__main__":
    TEST_RESULT = largest_number([23, 5, 8, 14, 63, 12, 45])
    print(f"Three largest numbers: {TEST_RESULT}")
