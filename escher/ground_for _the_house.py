

plan = ('''0000000
##00##0
######0
##00##0
#0000#0
''')
plan = [x for x in plan.split('\n') if x]

def house0(plan):
    up = down = left = right = None
    for row in range(len(plan)):
        print(row, 'строка')
        for col in range(len(plan[row])):
            if plan[row][col] == '#':
                if up == None:
                    up = down = row
                    left = right = col
                if col < left:
                    left = col
                if col > right:
                    right = col
                if row > up:
                    up = row
                if row < down:
                    print(row, col)
                    down = row
    if up == None:
        return 0
    return (up - down + 1) * (right - left + 1)


print(house0(plan))
print(plan)