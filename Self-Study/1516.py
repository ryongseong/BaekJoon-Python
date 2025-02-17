import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]
indegree = [0 for _ in range(N+1)]
cost = [0 for _ in range(N+1)]
result = [0 for _ in range(N+1)]
queue = deque()

for i in range(1, N+1):
    data = list(map(int, input().split()))[:-1]
    cost[i] = data[0]
    buildings = data[1:]

    for j in buildings:
        graph[j].append(i)
        indegree[i] += 1

for i in range(1, N+1):
    if indegree[i] == 0:
        queue.append(i)

while queue:
    x = queue.popleft()
    result[x] += cost[x]
    for i in graph[x]:
        indegree[i] -= 1
        result[i] = max(result[i], result[x])
        if indegree[i] == 0:
            queue.append(i)

for i in range(1, N+1):
    print(result[i])