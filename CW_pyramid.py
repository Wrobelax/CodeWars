def tower_builder(n_floors):
    """
    This is a function for returning a pyramid  from '*'.

    :param n_floors: Defines number of floors - items that will be returned.
    :return: printed list of strings that creates pyramid-like scheme.
    """

    chr_tree = []


    while len(chr_tree) <= n_floors-1:
            chr_tree.append(f"{' ' * (n_floors-1-(len(chr_tree)))}{'*' * ((((n_floors-1)*2)+1)-(2*(n_floors-1-(len(chr_tree)))))}{' ' * (n_floors-1-(len(chr_tree)))}")

    return print(*chr_tree, sep='\n')