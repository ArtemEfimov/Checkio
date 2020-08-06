def index_power(array, n):
    return array[n] ** n if n < len(array) else -1


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert index_power([1, 2, 3, 4], 2) == 9, "Square"
    assert index_power([1, 3, 10, 100], 3) == 1000000, "Cube"
    assert index_power([0, 1], 0) == 1, "Zero power"
    assert index_power([1, 2], 3) == -1, "IndexError"

