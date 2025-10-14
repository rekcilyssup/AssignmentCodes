"""Module for solving question 12 - Find substrings starting from vowels and consonants."""


def find_substrings(input_str):
    """
    Find all substrings starting from vowels and consonants.
    Input: "abcd"
    Output: {"vowel": ["a", "ab", "abc", "abcd"], "consonants": ["b", "c", "d", "bc", "cd", "bcd"]}

    Args:
        input_str (str): String to process
    Returns:
        dict: Dictionary with vowel and consonant substrings
    """
    vowels = "aeiouAEIOU"
    substrings = {"vowel": [], "consonants": []}

    # Generate all possible substrings
    for i in range(len(input_str)):
        for j in range(i + 1, len(input_str) + 1):
            substring = input_str[i:j]
            if substring[0] in vowels:
                substrings["vowel"].append(substring)
            else:
                substrings["consonants"].append(substring)

    return substrings


# Test the function
RESULT = find_substrings("abcd")
print(f"Substrings by type: {RESULT}")
