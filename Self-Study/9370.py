import sys
from heapq import heappush, heappop

input = sys.stdin.readline


def dijkstra(start_node):
    pq = [(0, start_node, 0)]
    dists = [[float("inf"), 0] for _ in range(n + 1)]
    dists[start_node] = [0, 0]

    while pq:
        dist, node, cnt = heappop(pq)
        if dists[node][0] < dist:
            continue

        for next_dist, next_node in graph[node]:
            new_dist = dist + next_dist
            if new_dist < dists[next_node][0]:
                dists[next_node] = [new_dist, dists[next_node][1] + 1]


for _ in range(int(input())):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, d = map(int, input().split())
        graph[a].append((d, b))
        graph[b].append((d, a))
    destinations = [int(input()) for _ in range(t)]
    dijkstra(s)
