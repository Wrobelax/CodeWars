def count_by(x:int, n:int) -> list:
    """
    Return a sequence of numbers counting by `x` `n` times.

    Args:
        x: Integer that the list starts counting from and defining by how much a next number in a list extends.
        n: Integer defining length of the list.

    Returns:
        new_list: A new list of n length counted by x.
    """
    new_list = []

    for i in range(x,(x*n)+x,x):
        if len(new_list) <= n:
            new_list.append(i)

    return new_list

print(count_by(1,5))
