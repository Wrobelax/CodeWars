def descending_order(num):
    """
    Function for sorting provided number in descending order.

    :param num: Integer to be sorted.
    :return: Sorted number as an integer.
    """
    numbers= f"{num}"
    number_list = list(numbers)
    number_list.sort(reverse=True)
    return_number = ""

    for number in number_list:
        return_number += number

    return int(return_number)