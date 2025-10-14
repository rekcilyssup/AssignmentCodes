"""Module for solving question 1 - Sum all items in a list."""


def sum_of_num(arr):
    """
    Sum all items in a list.
    Input: [2,5,8,9,21]
    Output: 45

    Args:
        arr (list): List of numbers
    Returns:
        int: Sum of all numbers in the list
    """
    total = 0
    for number in arr:
        total += number
    return total


# Test the function
if __name__ == "__main__":
    TEST_RESULT = sum_of_num([2, 5, 8, 9, 21])
    print(f"Sum: {TEST_RESULT}")
