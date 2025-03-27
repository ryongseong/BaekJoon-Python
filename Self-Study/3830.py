import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline


def find(x):
    if parent[x] != x:
        origin = parent[x]
        parent[x] = find(parent[x])
        weight[x] += weight[origin]
    return parent[x]


def union(a, b, w):
    ra = find(a)
    rb = find(b)
    if ra == rb:
        return
    parent[rb] = ra
    weight[rb] = weight[a] - weight[b] + w


while True:
    N, M = map(int, input().split())
    if N == M == 0:
        break

    parent = [i for i in range(N + 1)]
    weight = [0] * (N + 1)

    for _ in range(M):
        mark, *query = input().split()
        if mark == "!":
            a, b, w = map(int, query)
            union(a, b, w)
        elif mark == "?":
            a, b = map(int, query)
            if find(a) != find(b):
                print("UNKNOWN")
            else:
                print(weight[b] - weight[a])
