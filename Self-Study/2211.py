import sys
from heapq import heappop, heappush
input = sys.stdin.readline
INF = int(1e9)


def dijkstra(start):
    pq = [(0, start)]
    dists = [INF] * (N+1)
    dists[start] = 0

    while pq:
        dist, node = heappop(pq)

        if dists[node] < dist:
            continue

        for next_dist, next_node in graph[node]:
            new_dist = dist + next_dist
            if new_dist < dists[next_node]:
                dists[next_node] = new_dist
                parents[next_node] = node
                heappush(pq, (new_dist, next_node))


N, M = map(int, input().split())
parents = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

dijkstra(1)
print(N-1)
for i in range(2, N + 1):
    print(i, parents[i])
