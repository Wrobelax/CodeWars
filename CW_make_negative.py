def make_negative(number:float ) -> float:
    """Function for checking if a number is positive and if so, returning the same negative number.
    For negative numbers returns negative.

    Args:
        number: Number to be checked.

    Returns:
        x: Negative number.

    """
    if number > 0:
        x = number * -1

    else:
        x = number

    return x

print(make_negative(5))