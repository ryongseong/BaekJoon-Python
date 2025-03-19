def change_to_integer(c):
    return alpha[c]


alpha = {
    "A": 3,
    "B": 2,
    "C": 1,
    "D": 2,
    "E": 3,
    "F": 3,
    "G": 3,
    "H": 3,
    "I": 1,
    "J": 1,
    "K": 3,
    "L": 1,
    "M": 3,
    "N": 3,
    "O": 1,
    "P": 2,
    "Q": 2,
    "R": 2,
    "S": 1,
    "T": 2,
    "U": 1,
    "V": 1,
    "W": 2,
    "X": 2,
    "Y": 2,
    "Z": 1,
}


S = input().upper()
K = len(S)
lst = list(map(change_to_integer, S))
result = sum(lst) % 10
if result % 2 == 0:
    print("You're the winner?")
else:
    print("I'm a winner!")
