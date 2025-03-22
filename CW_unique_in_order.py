from typing import Union

def unique_in_order(sequence:Union[str | list]) -> list:
    """
    Function for returning unique list from a provided list or string.

    :param sequence: String or list.
    :return unique_list: List of unique characters that do not repeat in order. They may repeat in a list.
    """

    seq_list = list(sequence)
    unique_list = []

    for item in seq_list:
            if not item in unique_list or item != unique_list[-1]:
                unique_list.append(item)

    return unique_list