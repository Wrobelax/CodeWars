def DNA_strand(dna:str) -> str:
    """
    Function for returning a second string of DNA basing on provided data.

    :param dna: String, must be one of letters: A, T, C, G.
    :return: String, basing on provided letter: for "A" <-> "T", for "C" <-> "G".
    """

    dna_2 = ""

    for symbol in dna:
        if symbol == "A":
            dna_2 += "T"

        if symbol == "T":
            dna_2 += "A"

        if symbol == "C":
            dna_2 += "G"

        if symbol == "G":
            dna_2 += "C"

    return dna_2