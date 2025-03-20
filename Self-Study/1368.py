from heapq import heappop, heappush


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
pq = []
parents = [i for i in range(N + 1)]


for i in range(1, N + 1):
    heappush(pq, [int(input()), 0, i])

for i in range(1, N + 1):
    line = list(map(int, input().split()))
    for j in range(1, N + 1):
        if i == j:
            continue
        heappush(pq, [line[j - 1], i, j])

result = 0
while pq:
    w, u, v = heappop(pq)
    if find(u) != find(v):
        union(u, v)
        result += w

print(result)
