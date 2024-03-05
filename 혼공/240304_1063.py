# https://www.acmicpc.net/problem/1063

k, s, n = map(str, input().split())

xList = [8, 7, 6, 5, 4, 3, 2, 1]
yList = ["A", "B", "C", "D", "E", "F", "G", "H"]

stone = [xList.index(int(s[1])), yList.index(s[0])]
king = [xList.index(int(k[1])), yList.index(k[0])]

move = {
    "R": (0, 1),
    "L": (0, -1),
    "B": (1, 0),
    "T": (-1, 0),
    "RT": (-1, 1),
    "LT": (-1, -1),
    "RB": (1, 1),
    "LB": (1, -1)
}

for _ in range(int(n)):
    dx, dy = move[input()]
    
    kx = king[0] + dx
    ky = king[1] + dy
    if kx < 0 or kx >= 8 or ky < 0 or ky >= 8:
        continue

    if kx != stone[0] or ky != stone[1]:
        king = [kx, ky]
        continue

    sx = stone[0] + dx
    sy = stone[1] + dy
    if sx < 0 or sx >= 8 or sy < 0 or sy >= 8:
        continue

    stone = [sx, sy]
    king = [kx, ky]

print(yList[king[1]] + str(xList[king[0]]))
print(yList[stone[1]] + str(xList[stone[0]]))