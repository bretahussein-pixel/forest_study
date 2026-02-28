def calc_forest_area(width, length):
    """
    Docstring for calc_forest_area

    :param width: Description
    :param length: Description
    """
    area = width * length
    return area


nairobi_forest = calc_forest_area(300, 400)
print(nairobi_forest)
print(calc_forest_area.__doc__)
