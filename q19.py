"""Module docstring."""


def hotel_cost(nights):
    """Function to calculate hotel cost"""

    # write your code here
    return 140 * nights


def plane_ride_cost(city):
    """Function to calculate plane cost"""

    # write your code here
    prices = {"Charlotte": 183, "Tampa": 220, "Pittsburgh": 222, "Los Angeles": 475}
    if city in prices:
        return prices[city]
    return 0


def rental_car_cost(days):
    """Function to calculate car cost"""
    if days >= 7:
        return days * 40 - 50
    if days >= 3:
        return days * 40 - 20
    return days * 40


def trip_cost(input_list):
    """
    Accepts list of ["city",days,spending_money]
    returns output
    """
    total_sum = 0

    # Handle case where input_list might be a single trip instead of list of trips
    if input_list and len(input_list) == 3 and isinstance(input_list[0], str):
        # Single trip format: ["city", days, spending_money]
        input_list = [input_list]

    for trip in input_list:
        # Handle case where trip might be malformed
        if not isinstance(trip, (list, tuple)) or len(trip) < 3:
            continue

        city = trip[0]
        # Handle cases where days/spending_money might be strings or numbers
        try:
            days = int(trip[1]) if not isinstance(trip[1], int) else trip[1]
        except (ValueError, TypeError):
            days = 0

        try:
            spending_money = int(trip[2]) if not isinstance(trip[2], int) else trip[2]
        except (ValueError, TypeError):
            spending_money = 0

        # Hotel nights = days - 1 (you don't need hotel on the last day)
        nights = days - 1 if days > 0 else 0
        total_sum += (
            hotel_cost(nights)
            + plane_ride_cost(city)
            + rental_car_cost(days)
            + spending_money
        )
    # write your code here

    return total_sum


def test_trip_cost():
    """Test the trip_cost function."""
    test_list = [["Charlotte", 5, 100]]
    expected = hotel_cost(5) + plane_ride_cost("Charlotte") + rental_car_cost(5) + 100
    result = trip_cost(test_list)
    print(f"Input: {test_list}")
    print(f"Trip cost: {result}")
    print(f"Expected: {expected}")
    print(f"Test passed: {result == expected}")


if __name__ == "__main__":
    test_trip_cost()
