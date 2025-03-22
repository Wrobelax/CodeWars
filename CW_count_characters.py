def count(s:str) -> dict:
    """
    Function for counting letters from given word.

    :param s: String.
    :return: Dictionary with letters from a string as keys and number of letters appearance as a value.
    """
    
    letters_list = list(s)
    dictionary = {}

    for letter in letters_list:
        if not letter in dictionary:
            dictionary[letter] = 1

        else:
            dictionary[letter] += 1

    return dictionary