import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
indegree = [0 for _ in range(N+1)]
queue = deque()
result = []

for _ in range(M):
    data = list(map(int, input().split()))
    for i in range(1, data[0]):
        graph[data[i]].append(data[i+1])
        indegree[data[i+1]] += 1

for i in range(1, N+1):
    if indegree[i] == 0:
        queue.append(i)

while queue:
    x = queue.popleft()
    result.append(x)
    for i in graph[x]:
        indegree[i] -= 1

        if indegree[i] == 0:
            queue.append(i)

if len(result) != N:
    print(0)
else:
    for i in result:
        print(i)