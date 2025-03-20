import sys

input = sys.stdin.readline
INF = int(1e9)


def bf():
    dists[1] = 0

    for i in range(1, N + 1):
        for j in range(M):
            s, e, w = edges[j]
            if dists[s] != INF and dists[e] > dists[s] + w:
                dists[e] = dists[s] + w
                if i == N:
                    return True

    return False


N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]
dists = [INF] * (N + 1)

if bf():
    print(-1)
else:
    for i in range(2, N + 1):
        if dists[i] == INF:
            print(-1)
        else:
            print(dists[i])
