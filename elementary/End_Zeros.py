"""Try to find out how many zeros a given number has at the end. """


def end_zeros(num: int) -> int:
    """ Description """
    some_list = []
    while True:
        if num % 10 == 0 and num != 0:
            some_list.append(0)
            num //= 10
        elif num == 0:
            return 1
        else:
            break
    return len(some_list)


if __name__ == '__main__':
    print("Example:")
    print(end_zeros(100100))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert end_zeros(0) == 1
    assert end_zeros(1) == 0
    assert end_zeros(10) == 1
    assert end_zeros(101) == 0
    assert end_zeros(245) == 0
    assert end_zeros(100100) == 2
    print("Coding complete? Click 'Check' to earn cool rewards!")
