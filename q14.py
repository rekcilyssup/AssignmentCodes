"""Module docstring."""


def list_hex_dec_oct_bin(input_list):
    """
    Accepts an list as a parameter
    returns output

    """

    # Write your code
    result = []
    for i in input_list:
        decimal = str(i)
        octal = format(i, "o")
        hexadecimal = format(i, "x")
        binary = format(i, "b")
        result.append(f"{decimal}.{octal}.{hexadecimal}.{binary}")
    return result


def test_list_hex_dec_oct_bin():
    """Test the list_hex_dec_oct_bin function."""
    test_list = [15, 17, 18]
    expected = ["15.17.f.1111", "17.21.11.10001", "18.22.12.10010"]
    result = list_hex_dec_oct_bin(test_list)
    print(f"Input: {test_list}")
    print(f"Formatted: {result}")
    print(f"Expected: {expected}")
    print(f"Test passed: {result == expected}")


if __name__ == "__main__":
    test_list_hex_dec_oct_bin()
