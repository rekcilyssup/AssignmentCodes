"""Module for solving question 11 - Change character at given index."""


def change_char(input_list):
    """
    Change character at given index in string.
    Input: ["abcdefghijk", 5, "k"]
    Output: "abcdekghijk"

    Args:
        input_list (list): List containing [string, index, new_character]
    Returns:
        str: Modified string with character replaced
    """
    original_string = input_list[0]
    index = input_list[1]
    new_char = input_list[2]
    modified_string = original_string[:index] + new_char + original_string[index + 1 :]
    return modified_string


# Test the function
test_input = ["abcdefghijk", 5, "k"]
RESULT = change_char(test_input)
print(f"Modified string: {RESULT}")
