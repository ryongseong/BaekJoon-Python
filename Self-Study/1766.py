import heapq
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
indegree = [0 for _ in range(N+1)]
result = []
queue = []

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    indegree[B] += 1

for i in range(1, N+1):
    if indegree[i] == 0:
        heapq.heappush(queue, i)

while queue:
    temp = heapq.heappop(queue)
    result.append(temp)
    for i in graph[temp]:
        indegree[i] -= 1
        if indegree[i] == 0:
            heapq.heappush(queue, i)

print(*result)