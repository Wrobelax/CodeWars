def xo(s:str) -> bool:
    """
    Function for checking number of "x" and "o" in a given string and comparing if they are the same.

    :param s:Sting to be checked.
    :return: Bool -> true if number of "x" = "o". False if not.
    """
    x = 0
    o = 0
    for i in s:
        if i.lower() =="x":
            x += 1
        elif i.lower() =="o":
            o += 1
        else:
            pass

    if x == o:
        return True
    else:
        return False
