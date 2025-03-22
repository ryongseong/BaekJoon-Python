import sys
from heapq import heappush, heappop

sys.setrecursionlimit(10**6)

input = sys.stdin.readline
INF = int(1e9)


def dijkstra(start_node):
    pq = [(0, start_node)]
    dists = [INF] * (n + 1)
    dists[start_node] = 0

    while pq:
        dist, node = heappop(pq)
        if dists[node] < dist:
            continue
        for next_dist, next_node in graph[node]:
            new_dist = dist + next_dist
            if new_dist < dists[next_node]:
                dists[next_node] = new_dist
                heappush(pq, (new_dist, next_node))

    return dists


for _ in range(int(input())):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, d = map(int, input().split())
        graph[a].append((d, b))
        graph[b].append((d, a))
    destinations = [int(input()) for _ in range(t)]
    s_dijk = dijkstra(s)
    g_dijk = dijkstra(g)
    h_dijk = dijkstra(h)
    result = []
    for d in destinations:
        if (
            s_dijk[g] + g_dijk[h] + h_dijk[d] == s_dijk[d]
            or s_dijk[h] + h_dijk[g] + g_dijk[d] == s_dijk[d]
        ):
            result.append(d)

    print(*sorted(result))
