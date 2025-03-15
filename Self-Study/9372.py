def dfs(node, cnt):
    visited[node] = 1
    for x in graph[node]:
        if not visited[x]:
            cnt = dfs(x, cnt + 1)
    return cnt


for _ in range(int(input())):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N + 1)]

    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    visited = [0] * (N + 1)
    print(dfs(1, 0))
