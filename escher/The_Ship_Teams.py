from bisect import insort_left

sailors = {
    'Smith': 34,
    'Wesson': 22,
    'Coleman': 45,
    'Abrahams': 19}


def two_teams(sailors: dict):
    ships = [[], []]
    for sailor, age in sailors.items():
        insort_left(ships[20 <= age <= 40], sailor)
    return ships

# def two_teams(sailors):
#     return [sorted(sailor for sailor,age in sailors.items() if age < 20 or age > 40),
#             sorted(sailor for sailor,age in sailors.items() if 20 <= age <= 40)]
#сортировка матросов на 2 команды по возрасту.

print(two_teams(sailors))