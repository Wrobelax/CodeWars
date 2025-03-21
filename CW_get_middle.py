def get_middle(s:str) -> str:
    """
    Function for checking number of letters in a word and returning, either middle letter if odd or two middle letters if even.

    :param s: String to be checked.
    :return: Sliced string.
    """

    if len(s) % 2 == 0:
        indx = int(len(s)/2)
        return (s[indx-1:indx+1])
    else:
        indx = int(len(s) / 2)
        return (s[indx])