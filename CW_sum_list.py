def sum_array(arr:list):
    #your code here
    """Function for removing the highest and smallest number from the list and returning a sum of the remainings.

    Args:
        arr: Argument accepting a list. For None, blank list or a list with only one element returns 0.

    Returns:
        Sum of a list without a lowest and a highest element.

    """
    if arr == None or arr == []:
        return 0

    elif len(arr) == 1:
        return 0

    else:
        len(arr) > 1
        arr.remove(min(arr))
        arr.remove(max(arr))
    return sum(arr)


print(sum_array([3, 2, 28, 1, 11]))
