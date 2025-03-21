def is_isogram(string:str) -> bool:
    """
    Function for checking if a word is an isogram - has all letters unique.

    :param string: String to be checked. Uppercase ignored.
    :return: Bool -> True if a string is an isogram. False if not.
    """
    count_list =[]
    letters_list = list(string.lower())

    for letter in letters_list:
        count = letters_list.count(letter)
        count_list.append(count)

    for number in count_list:
        if number > 1:
            return False

    return True