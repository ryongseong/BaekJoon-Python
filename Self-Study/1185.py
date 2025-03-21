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


N, P = map(int, input().split())
parents = [i for i in range(N + 1)]
costs = [float("inf")] + [int(input()) for _ in range(N)]
edges = []

for _ in range(P):
    a, b, c = map(int, input().split())
    edges.append([a, b, costs[a] + costs[b] + 2 * c])
edges.sort(key=lambda x: x[2])
answer = min(costs)
check = 1
for a, b, w in edges:
    if find(a) != find(b):
        union(a, b)
        answer += w
        check += 1
        if check == N:
            break

print(answer)
