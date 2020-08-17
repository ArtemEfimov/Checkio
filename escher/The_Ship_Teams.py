from bisect import insort_left

sailors = {
    'Smith': 34,
    'Wesson': 22,
    'Coleman': 45,
    'Abrahams': 19}


def two_teams(sailors: dict):
    """ Description """
    ships = [[], []]
    for sailor, age in sailors.items():
        insort_left(ships[20 <= age <= 40], sailor)
    return ships

print(two_teams(sailors))
