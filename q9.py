"""Module docstring."""


def swap_case(input_str):
    """
    Accepts an string as a parameter
    returns output

    """

    # Write your code
    result = ""
    for i in input_str:
        if i.islower():
            result += i.upper()
        else:
            result += i.lower()

    return result


def test_swap_case():
    """Test the swap_case function."""
    test_string = "Hello World"
    expected = "hELLO wORLD"
    result = swap_case(test_string)
    print(f"Input: {test_string}")
    print(f"Swapped case: {result}")
    print(f"Expected: {expected}")
    print(f"Test passed: {result == expected}")


if __name__ == "__main__":
    test_swap_case()
