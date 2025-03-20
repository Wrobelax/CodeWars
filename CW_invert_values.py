def invert(lst:list) -> list:
    """
    Function for returning inversed numbers from a list.
    For x negative -> x positive
    For x positive -> x negative

    :param lst: List ti be inverted.
    :return: Inverted list.
    """

    new_list = []

    for i in lst:
        i = i * -1
        new_list.append(i)

    return new_list

print(invert([]))