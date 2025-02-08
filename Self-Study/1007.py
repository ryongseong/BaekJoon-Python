from math import sqrt
from itertools import combinations

T = int(input())

for _ in range(T):
    N = int(input())
    point_list = []
    process_x, process_y = 0, 0
    for _ in range(N):
        x1, y1 = map(int, input().split())
        process_x += x1
        process_y += y1
        point_list.append((x1, y1))

    combs = list(combinations(point_list, N // 2))
    result = 3e5

    for comb in combs[:len(combs)// 2]:
        x1, y1 = 0, 0
        for x, y in comb:
            x1 += x
            y1 += y
        x2, y2 = process_x - x1, process_y - y1

        vector = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        result = min(result, vector)

    print(result)