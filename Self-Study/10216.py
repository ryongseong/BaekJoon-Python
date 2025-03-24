from math import sqrt
import sys

input = sys.stdin.readline


def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]


def union(a, b):
    a, b = find(a), find(b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b


for _ in range(int(input())):
    N = int(input())
    parents = [i for i in range(N)]
    point_list = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        x1, y1, r1 = point_list[i]
        for j in range(i + 1, N):
            x2, y2, r2 = point_list[j]
            if find(i) == find(j):
                continue
            if sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2) <= r1 + r2:
                union(i, j)

    cnt_group = set()
    for i in range(N):
        x = find(i)
        if x not in cnt_group:
            cnt_group.add(x)

    print(len(cnt_group))
