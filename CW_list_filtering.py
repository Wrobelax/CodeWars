def filter_list(l:list) -> list:
    """Function for returning a new list with the strings filtered out.

    :param
        l: List with integers and strings.

    :return
        int_list: List with integers only.

    """
    int_list = []

    for i in l:
        try:
            if i >= 0:
                int_list.append(i)
        except TypeError:
            pass

    return int_list

print(filter_list([1, "a", "b", 0, 15]))
