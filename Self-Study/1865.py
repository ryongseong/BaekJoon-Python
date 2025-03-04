for _ in range(int(input())):
    N, M, W = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        s, e, t = map(int, input().split())
        graph[s].append((e, t))
        graph[e].append((s, t))
