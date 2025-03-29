import sys
from heapq import heappop, heappush

input = sys.stdin.readline


def dijkstra(start):
    pq = []

    for i in range(1, n + 1):
        if i != start:
            heappush(pq, (dists[start][i], i))

    while pq:
        dist, node = heappop(pq)

        if dists[start][node] < dist:
            continue

        for nxt in range(1, n + 1):
            if node == nxt or start == nxt:
                continue
            if dist + dists[node][nxt] < dists[start][nxt]:
                dists[start][nxt] = dist + dists[node][nxt]
                heappush(pq, (dist + dists[node][nxt], nxt))
                result[start][nxt] = result[start][node]


n, m = map(int, input().split())
dists = [[float("inf")] * (n + 1) for _ in range(n + 1)]
result = [["-"] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    s, e, w = map(int, input().split())
    dists[s][e] = dists[e][s] = w
    result[s][e] = str(e)
    result[e][s] = str(s)


for i in range(1, n + 1):
    dijkstra(i)

for arr in result[1:]:
    print(*arr[1:])
