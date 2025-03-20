import sys
from heapq import heappop, heappush

input = sys.stdin.readline


def dijkstra(start):
    pq = [(0, start)]
    dists = [float("inf")] * (N + 1)
    dists[start] = 0

    while pq:
        dist, node = heappop(pq)

        if dists[node] < dist:
            continue

        for next_dist, next_node in graph[node]:
            new_dist = dist + next_dist
            if dists[next_node] > new_dist:
                dists[next_node] = new_dist
                heappush(pq, (new_dist, next_node))

    result = [idx for idx, i in enumerate(dists) if i == K]
    return result if result else [-1]


N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append((1, b))

result = dijkstra(X)
result.sort()
for i in result:
    print(i)
