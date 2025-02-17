import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    D = [0] + list(map(int, input().split()))

    graph = [[] for _ in range(N+1)]
    indegree = [0 for _ in range(N+1)]
    dp = [0 for _ in range(N+1)]
    queue = deque()

    for _ in range(K):
        x, y = map(int, input().split())
        graph[x].append(y)
        indegree[y] += 1
    W = int(input())

    for i in range(1, N+1):
        if indegree[i] == 0:
            queue.append(i)
            dp[i] = D[i]
    
    while queue:
        x = queue.popleft()
        for i in graph[x]:
            indegree[i] -= 1
            dp[i] = max(dp[x]+D[i], dp[i])
            if indegree[i] == 0:
                queue.append(i)

    print(dp[W])