from collections import deque

N, M = map(int, input().split())
graphs = [[] for _ in range(N + 1)]
indegree = [0 for _ in range(N + 1)]
dp = [1 for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graphs[a].append(b)
    indegree[b] += 1

queue = deque()
for i in range(1, N + 1):
    if indegree[i] == 0:
        queue.append(i)

while queue:
    x = queue.popleft()
    for i in graphs[x]:
        indegree[i] -= 1
        dp[i] = dp[x] + 1
        if indegree[i] == 0:
            queue.append(i)

print(*dp[1:])
