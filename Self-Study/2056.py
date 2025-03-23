import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
indegree = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]
dp = [0] * (N + 1)
t = [0]

for i in range(1, N + 1):
    arr = list(map(int, input().split()))
    t.append(arr[0])
    if arr[1] != 0:
        for j in range(2, len(arr)):
            graph[arr[j]].append(i)
            indegree[i] += 1

queue = deque()
for i in range(1, N + 1):
    if indegree[i] == 0:
        queue.append(i)
        dp[i] = t[i]

while queue:
    now = queue.popleft()
    for x in graph[now]:
        indegree[x] -= 1
        dp[x] = max(dp[now] + t[x], dp[x])
        if indegree[x] == 0:
            queue.append(x)

print(max(dp))
