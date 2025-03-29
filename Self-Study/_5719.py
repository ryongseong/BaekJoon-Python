from copy import deepcopy
import sys
from heapq import heappush, heappop

input = sys.stdin.readline

INF = int(1e9)


def dfs(node, cost, visited):
    global min_cost

    if cost > min_cost:
        return

    if node == D and min_cost != INF:
        return visited


def dijkstra():
    pq = [(0, S)]
    dists = [INF] * N
    dists[S] = 0

    while pq:
        dist, node = heappop(pq)

        if dists[node] < dist:
            continue

        for i in range(N):
            pass


while True:
    N, M = map(int, input().split())
    if N == M == 0:
        break

    graph = [[INF] * N for _ in range(N)]
    S, D = map(int, input().split())

    min_cost = INF

    for _ in range(M):
        U, V, P = map(int, input().split())
        graph[U][V] = P

    second_graph = deepcopy(graph)

    visited_path = dfs(S, 0, set())

    print(second_graph)
