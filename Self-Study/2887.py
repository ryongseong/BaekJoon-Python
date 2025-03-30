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
parents = [i for i in range(N)]
points = []
edges = []

for i in range(N):
    x, y, z = map(int, input().split())
    points.append((i, x, y, z))

for axis in range(1, 4):
    points.sort(key=lambda x: x[axis])
    for i in range(N - 1):
        a, b = points[i], points[i + 1]
        cost = abs(a[axis] - b[axis])
        edges.append((cost, a[0], b[0]))

edges.sort()

cost = 0
for w, s, e in edges:
    if find(s) != find(e):
        union(s, e)
        cost += w

print(cost)
