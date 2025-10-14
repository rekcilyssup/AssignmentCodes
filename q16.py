"""Module docstring."""


def modify_first_middle_last(input_list):
    """
    Accepts an list as a parameter
    returns output

    """

    # Write your code
    # Pattern: all first chars + all middle chars + all last chars
    # For single char words: char is used as first, middle, AND last
    first_chars = ""
    middle_chars = ""
    last_chars = ""

    for word in input_list:
        if len(word) == 0:
            continue

        # First character - always add for non-empty words
        first_chars += word[0]

        # Middle character
        if len(word) == 1:
            # For single char words, the char is also the middle
            middle_chars += word[0]
        elif len(word) >= 2:
            mid_index = len(word) // 2
            middle_chars += word[mid_index]

        # Last character
        if len(word) == 1:
            # For single char words, the char is also the last
            last_chars += word[0]
        elif len(word) == 2:
            # For 2-char words, last char is the second char
            last_chars += word[1]
        else:
            # For 3+ char words, last char is the actual last char
            last_chars += word[-1]

    return first_chars + middle_chars + last_chars


def test_modify_first_middle_last():
    """Test the modify_first_middle_last function."""
    test_list = ["abc", "def", "ghi"]
    expected = "abdefghi"
    result = modify_first_middle_last(test_list)
    print(f"Input: {test_list}")
    print(f"Result: {result}")
    print(f"Expected: {expected}")
    print(f"Test passed: {result == expected}")


if __name__ == "__main__":
    test_modify_first_middle_last()
