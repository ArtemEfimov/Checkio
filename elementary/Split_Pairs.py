"""
 Split the string into pairs of two characters.
 If the string contains an odd number of characters,
 then the missing second character of the final pair should be replaced with an underscore ('_').

"""
from typing import List


def split_pairs(a: str) -> List[str]:
    """ Description """
    return ["".join(i) for i in zip(a[::2], a[1::2] + "_")]


if __name__ == "__main__":
    assert list(split_pairs("abcd")) == ["ab", "cd"]
    assert list(split_pairs("abc")) == ["ab", "c_"]
    assert list(split_pairs("abcdf")) == ["ab", "cd", "f_"]
    assert list(split_pairs("a")) == ["a_"]
    assert list(split_pairs("")) == []
    print("PASSED!!!")
