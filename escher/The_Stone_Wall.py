"""
As input you'll get a multiline string consists of '0' and '#' - a view of a stone wall from above.
The '#' will show the stone part of the wall and the '0' will show the empty part.
The relative location of you and the wall is as follows: you look at the array from the bottom of it.
Your task is to find the index of the place where the wall is the narrowest (as shown at the picture below).
The width of the wall is the height of the columns of the array (multiline string). If there are several such places,
return the index of leftmost. Index starts from 0.
"""


def stone_wall(wall):
    """ Description """

    wall = [x for x in wall.split('\n') if len(x) > 0]  # ['##########', '####0##0##', '00##0###00']
    rot_wall = ['' for _ in range(len(wall[0]))]  # ['', '', '', '', '', '', '', '', '', '']
    for i in range(len(wall)):
        for j in range(len(wall[0])):
            rot_wall[j] += wall[i][j]  # ['##0', '##0', '###', '###', '#00', '###', '###', '#0#', '##0', '##0']

    def conv(val: str):
        """Count values"""
        return val.count('#')

    new_list = list(map(conv, rot_wall))
    return new_list.index(min(new_list))


if __name__ == '__main__':
    print("Example:")
    print(stone_wall('''
##########
####0##0##
00##0###00
'''))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert stone_wall('''
##########
####0##0##
00##0###00
''') == 4

    assert stone_wall('''
#00#######
#######0##
00######00
''') == 1

    assert stone_wall('''
#####
#####
#####
''') == 0

print("Coding complete? Click 'Check' to earn cool rewards!")

