def check(seq:list, elem) -> bool:
    """
    Function for checking if an element is present in given list.

    :param seq: List to be checked. Function will iterate over it.
    :param elem: Element to be checked if is present in a function.

    :return: True or False
    """
    
    for i in seq:
        if i == elem:
            return True

    return False

