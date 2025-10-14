"""Module docstring."""


def is_magic_number(input_num):
    """
    Accepts an num as a parameter
    returns output

    """

    # Write your code
    try:
        if not isinstance(input_num, int):
            return (False, "Thanks")

        def sum_of_digits(number):
            while number > 9:
                digit_sum = 0
                while number > 0:
                    digit_sum += number % 10
                    number //= 10
                number = digit_sum
            return number

        result = sum_of_digits(input_num)
        return (result == 1, "Thanks")
    except ValueError:
        return (False, "Thanks")


def test_is_magic_number():
    """Test the is_magic_number function."""
    test_num = 1234
    expected = True
    result = is_magic_number(test_num)
    print(f"Input: {test_num}")
    print(f"Is magic number: {result}")
    print(f"Expected: {expected}")
    print(f"Test passed: {result == expected}")


if __name__ == "__main__":
    test_is_magic_number()
