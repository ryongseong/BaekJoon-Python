import heapq
import sys

input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    A, B, C = map(int, input().split())
    graph[A].append([B, C])

start, end = map(int, input().split())

costs = [float('inf')] * (N+1)
heap = [(0, start)]
costs[start] = 0

while heap:
    cost, v = heap.heappop(heap)
    if costs[v] < cost:
        continue

    for n_v, n_cost in graph[v]:
        sum_cost = cost + n_cost
        if sum_cost < costs[n_v]:

            costs[n_v] = sum_cost
            heapq.heappush(heap, (sum_cost, n_v))

print(costs[end])