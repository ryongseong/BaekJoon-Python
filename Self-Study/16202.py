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


N, M, K = map(int, input().split())
edges = []

for i in range(1, M + 1):
    a, b = map(int, input().split())
    edges.append((a, b, i))

edges.sort(key=lambda x: x[2])

for j in range(K):
    cnt = 0
    cost = 0
    parents = [i for i in range(N + 1)]

    for s, e, w in edges:
        if find(s) != find(e):
            union(s, e)
            cost += w
            cnt += 1

    if cnt != (N - 1):
        for _ in range(K - j):
            print(0, end=" ")
        exit()
    else:
        print(cost, end=" ")
    edges.pop(0)
