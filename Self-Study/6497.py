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


while True:
    m, n = map(int, input().split())
    if m == n == 0:
        break
    parents = [i for i in range(m)]
    edges = []
    min_cost = 0
    for _ in range(n):
        x, y, z = map(int, input().split())
        edges.append((z, x, y))

    edges.sort()

    for edge in edges:
        cost, x, y = edge
        if find(x) != find(y):
            union(x, y)
        else:
            min_cost += cost

    print(min_cost)
