def maps(a:list) -> list:
    """Returning a new list multiplied by 2

    Args:
        a: A list to be multiplied

    Returns:
        new_list: New list multiplied by 2
    """
    new_list =[]
    for i in a:
        new_list.append(i*2)

    return new_list

print(maps([]))