def lovefunc(flower1:int, flower2:int) -> bool:
    """Function for returning true if one of numbers given is even and another odd. If both are even/odd function returns false.

    Args:
        flower1: Integer
        flower2: Integer

    Returns:
        True or False

        """

    if flower1 % 2 ==0 and flower2 % 2 != 0:
        return True

    elif flower2 % 2 ==0 and flower1 % 2 != 0:
        return True
    else:
        return False

print(lovefunc(3,6))