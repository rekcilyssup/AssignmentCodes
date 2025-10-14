"""Module docstring."""


def calc_second_lowest_grade(input_list):
    """
    Accepts an list as a parameter
    returns list if second lowest grade

    """

    # Write your code
    # Grades: A=best (highest), F=worst (lowest)
    # A < B < C < D < E < F (lexicographically, A is best)
    # "Second lowest grade" means second worst grade

    # Get all unique grades and sort them alphabetically (A, B, C, D, E, F)
    # This gives us best to worst order
    all_grades = sorted(set(grade for _, grade in input_list))

    if len(all_grades) < 2:
        return []

    # Second lowest (second worst) grade is second from the end
    # If grades are [A, B, C, E], then E=worst, C=second worst
    second_lowest_grade = all_grades[-2]

    result_names = [
        [name, grade]
        for name, grade in input_list
        if grade == second_lowest_grade
    ]

    return result_names


def test_calc_second_lowest_grade():
    """Test the calc_second_lowest_grade function."""
    test_list = [["Alice", "B"], ["Bob", "A"], ["Charlie", "C"], ["David", "A"]]
    expected = [["Alice", "B"]]
    result = calc_second_lowest_grade(test_list)
    print(f"Input: {test_list}")
    print(f"Second lowest grade students: {result}")
    print(f"Expected: {expected}")
    print(f"Test passed: {result == expected}")


if __name__ == "__main__":
    test_calc_second_lowest_grade()
