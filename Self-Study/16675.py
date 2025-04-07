def convert_string_to_number(c):
    if c == "S":
        return 0
    elif c == "R":
        return 1
    elif c == "P":
        return 2


def who_is_winner(ml, mr, tl, tr):
    if ((ml - tl) in (-2, 1) and (ml - tr) in (-2, 1)) or (
        (mr - tl) in (-2, 1) and (mr - tr) in (-2, 1)
    ):
        return "MS"
    elif ((tl - ml) in (-2, 1) and (tl - mr) in (-2, 1)) or (
        (tr - ml) in (-2, 1) and (tr - mr) in (-2, 1)
    ):
        return "TK"
    return "?"


ml, mr, tl, tr = map(convert_string_to_number, input().split())
print(who_is_winner(ml, mr, tl, tr))
