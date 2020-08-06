

def easy_unpack(elements: tuple):
    """
        returns a tuple with 3 elements - first, third and second to the last
    """
    return tuple(elements[i] for i in [0, 2, -2])


easy_unpack((1, 2, 3, 4, 5, 6, 7, 9))




