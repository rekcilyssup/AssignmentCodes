"""Module for solving question 2 - Count alphabetic characters in string."""


def count_char(input_string):
    """
    Count the number of alphabetic characters in a string.
    Input: "abcdef2j3j4j5j"
    Output: 10

    Args:
        input_string (str): String to count alphabetic characters from
    Returns:
        int: Count of alphabetic characters
    """
    count = 0
    for character in input_string:
        if character.isalpha():
            count += 1
    return count


# Test the function
if __name__ == "__main__":
    TEST_RESULT = count_char("abcdef2j3j4j5j")
    print(f"Alphabetic character count: {TEST_RESULT}")
