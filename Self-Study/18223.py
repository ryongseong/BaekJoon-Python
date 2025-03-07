import heapq


def dijkstra(start):
    heap = []
    dist = [float("inf") for _ in range(V + 1)]
    heapq.heappush(heap, [0, start])
    dist[start] = 0
    while heap:
        cur_c, cur_v = heapq.heappop(heap)
        for next_v, next_c in graph[cur_v]:
            next_cost = cur_c + next_c
            if dist[next_v] > next_cost:
                dist[next_v] = next_cost
                heapq.heappush(heap, [next_cost, next_v])
    return dist


V, E, P = map(int, input().split())
graph = [[] for _ in range(V + 1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

if dijkstra(1)[V] == dijkstra(1)[P] + dijkstra(P)[V]:
    print("SAVE HIM")
else:
    print("GOOD BYE")
