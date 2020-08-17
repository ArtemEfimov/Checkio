"""
Your task is to count the sum of the number of steps required to pick up all 3 items - ('C' - compass), ('M' - map),
('S' - spyglass) from your starting position.
So the result will be the sum of distance from Y to C, from Y to M and from Y to S (not Y-C-M-S).
Note that you can walk in 8 directions - left, right, up, down and sideways (on the diagonal in any direction).
 Your starting position is 'Y'.
"""


def navigation(seaside):
    """ Description """
    y, c, m, s = [0, 0], [0, 0], [0, 0], [0, 0]
    for row, _ in enumerate(seaside):
        for column, _ in enumerate(seaside[row]):
            if seaside[row][column] == 'Y':
                y = [row, column]
            if seaside[row][column] == 'C':
                c = [row, column]
            if seaside[row][column] == 'M':
                m = [row, column]
            if seaside[row][column] == 'S':
                s = [row, column]

    distance = 0
    distance += max(abs(y[0] - c[0]), abs(y[1] - c[1]))
    distance += max(abs(y[0] - m[0]), abs(y[1] - m[1]))
    distance += max(abs(y[0] - s[0]), abs(y[1] - s[1]))
    return distance


if __name__ == '__main__':
    print("Example:")
    print(navigation([['Y', 0, 0, 0, 'C'],
                      [0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0],
                      ['M', 0, 0, 0, 'S']]))

# These "asserts" using only for self-checking and not necessary for auto-testing
assert navigation([['Y', 0, 0, 0, 'C'],
                   [0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0],
                   ['M', 0, 0, 0, 'S']]) == 11

assert navigation([[0, 0, 'C'],
                   [0, 'S', 0],
                   ['M', 'Y', 0]]) == 4

assert navigation([[0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 'M', 0, 'S', 0],
                   [0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 'C', 0, 0, 0],
                   [0, 'Y', 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0]]) == 9
print("Coding complete? Click 'Check' to earn cool rewards!")
