import sys
from collections import defaultdict
from heapq import heappush, heappop

input = sys.stdin.readline


def dijkstra(s):
    pq = [(0, s)]
    dists[s] = 0

    while pq:
        dist, node = heappop(pq)

        if dists[node] < dist:
            continue

        for next_dist, next_node in graph[node]:
            new_dist = dist + next_dist
            if new_dist < dists[next_node]:
                dists[next_node] = new_dist
                prev_node[next_node] = node
                heappush(pq, (new_dist, next_node))


N = int(input())
M = int(input())
INF = int(1e9)
dists = [INF] * (N + 1)
prev_node = [0] * (N + 1)

graph = defaultdict(list)
for _ in range(M):
    s, e, w = map(int, input().split())
    graph[s].append((w, e))
s, e = map(int, input().split())

dijkstra(s)
print(dists[e])
path = [e]
now = e
while now != s:
    now = prev_node[now]
    path.append(now)


path.reverse()

print(len(path))
print(*path)
