def count_positives_sum_negatives(arr:list) -> list:
    """Function for returning of count of positive numbers and a sum of negative numbers from a list.
    For empty list returns empty list.
    For all 0 returns [0,0].

    Args:
        arr: List to be provided.

    Returns:
        new_list: First item is a count of positive numbers. Second item is a sum of negative numbers.
    """

    new_list = [] #New list that will be returned
    list1 = [] #List of positive numbers
    list2 = [] #List of negative numbers

    # Iterating through elements from provided list and appending to a list1 if positive number or list2 if negative number.
    for i in arr:
        if i > 0:
            list1.append(i)

        elif i < 0:
            list2.append(i)

    # Checking lenght of lists and appending them whether any is longer than 0
    if len(list1) > 0 or len(list2) > 0:
        x = len(list1)
        new_list.append(x)
        print(list1)

        y = sum(list2)
        new_list.append(y)
        print(list2)

    # Checking if a list is not empty and whether all numbers are 0. If so, appends [0,0]
    if all(i == 0 for i in arr) and len(arr) > 0:
        new_list.extend([0,0])

    return new_list


print(count_positives_sum_negatives([0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14]))
