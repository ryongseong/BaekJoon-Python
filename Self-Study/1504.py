import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)


def dijkstra(start, end):
    distance = [INF for _ in range(N+1)]
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0

    while queue:
        dist, now = heapq.heappop(queue)

        if distance[now] < dist:
            continue

        for n, c in graph[now]:
            cost = distance[now] + c

            if distance[n] > cost:
                distance[n] = cost
                heapq.heappush(queue, (cost, n))

    return distance[end]

N, E = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

v1_dist = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, N)
v2_dist = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, N)

if v1_dist >= INF and v2_dist >= INF:
    print(-1)
else:
    print(min(v1_dist, v2_dist))