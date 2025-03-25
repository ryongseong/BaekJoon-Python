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


N = int(input())
parents = [i for i in range(N + 1)]
for _ in range(N - 2):
    i, j = map(int, input().split())
    union(i, j)

for i in range(2, N + 1):
    if find(1) != find(i):
        print(1, i)
        break
