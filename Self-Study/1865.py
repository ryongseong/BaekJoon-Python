def bf():
    for i in range(N):
        for j in range(len(edges)):
            cur, next, cost = edges[j]
            next_cost = dist[cur] + cost
            if dist[next] > next_cost:
                dist[next] = next_cost
                if i == N - 1:
                    return True

    return False


for _ in range(int(input())):
    N, M, W = map(int, input().split())
    edges = []
    dist = [1e9 for _ in range(N + 1)]
    for i in range(M + W):
        s, e, t = map(int, input().split())
        if i >= M:
            t = -t
        else:
            edges.append((e, s, t))
        edges.append((s, e, t))

    print("YES" if bf() else "NO")
