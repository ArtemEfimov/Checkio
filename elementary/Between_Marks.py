"""

You are given a string and two markers (the initial one and final).
You have to find a substring enclosed between these two markers.
But there are a few important conditions. """

import re


def between_markers(text: str, begin: str, end: str) -> str:
    """
        My solution
    """

    pattern = r'\b[Aa]\w+'
    a = re.findall(pattern, text)
    if len(a) > 1:
        return ' '.join(a)
    return '' if not a else a[0].lstrip(begin).rstrip(end)


#
# def between_markers(text: str, begin: str, end: str) -> str:
#     """
#         returns substring between two given markers
#     """
#     return text[text.index(begin) + 1:text.index(end)]
#

if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))

    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple"
    assert between_markers('What is [apple]', '[', ']') == "apple"
    assert between_markers('What is ><', '>', '<') == ""
    assert between_markers('>apple<', '>', '<') == "apple"
    print('Wow, you are doing pretty good. Time to check it!')
