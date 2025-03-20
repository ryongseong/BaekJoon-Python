import sys
from heapq import heappop, heappush

INF = int(1e9)
input = sys.stdin.readline


def dijkstra(s):
    pq = [(-INF, s)]
    dists = [0] * (N + 1)
    dists[s] = INF

    while pq:
        dist, node = heappop(pq)
        dist = -dist
        if dists[node] > dist:
            continue

        for next_dist, next_node in edges[node]:
            new_dist = min(dist, next_dist)
            if new_dist > dists[next_node]:
                dists[next_node] = new_dist
                heappush(pq, (-new_dist, next_node))

    return dists[e]


N, M = map(int, input().split())
s, e = map(int, input().split())
edges = [[] for _ in range(N + 1)]

for _ in range(M):
    h1, h2, k = map(int, input().split())
    edges[h1].append((k, h2))
    edges[h2].append((k, h1))

print(dijkstra(s))
