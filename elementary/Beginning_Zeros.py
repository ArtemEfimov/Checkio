"""You have a string that consist only of digits.
 You need to find how many zero digits ("0") are at the beginning of the given string. """


def beginning_zeros(number: str) -> int:
    """ Description """
    en = enumerate(number)
    if not int(number) and len(number) > 1:
        return len(number)
    return not int(number) or next(i for i, x in en if x != '0')


if __name__ == '__main__':
    print("Example:")
    print(beginning_zeros('100'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert beginning_zeros('100') == 0
    assert beginning_zeros('001') == 2
    assert beginning_zeros('100100') == 0
    assert beginning_zeros('001001') == 2
    assert beginning_zeros('012345679') == 1
    assert beginning_zeros('0000') == 4
    print("Coding complete? Click 'Check' to earn cool rewards!")
