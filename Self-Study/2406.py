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


n, m = map(int, input().split())
parents = [i for i in range(1001)]
for _ in range(m):
    a, b = map(int, input().split())
    union(a, b)

costs = [list(map(int, input().split())) for _ in range(n)]
edges = []

for i in range(1, n):
    for j in range(i + 1, n):
        edges.append((costs[i][j], i + 1, j + 1))

edges.sort()

total = 0
cnt = 0
arr = []

for w, s, e in edges:
    if find(s) != find(e):
        union(s, e)
        total += w
        arr.append((s, e))
        cnt += 1

print(total, cnt)
if cnt:
    for r in arr:
        print(*r)
