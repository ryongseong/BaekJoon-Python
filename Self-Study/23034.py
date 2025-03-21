import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())

edges = []
for _ in range(M):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

parent = [i for i in range(N + 1)]


def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x


def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return False
    parent[y] = x
    return True


mst_edges = [[] for _ in range(N + 1)]
total_cost = 0

edges.sort()
for cost, u, v in edges:
    if union(u, v):
        total_cost += cost
        mst_edges[u].append((v, cost))
        mst_edges[v].append((u, cost))

LOG = 17
depth = [0] * (N + 1)
up = [[0] * LOG for _ in range(N + 1)]
max_edge = [[0] * LOG for _ in range(N + 1)]


def dfs(node, par):
    for nxt, w in mst_edges[node]:
        if nxt != par:
            depth[nxt] = depth[node] + 1
            up[nxt][0] = node
            max_edge[nxt][0] = w
            dfs(nxt, node)


dfs(1, 0)

for k in range(1, LOG):
    for v in range(1, N + 1):
        up[v][k] = up[up[v][k - 1]][k - 1]
        max_edge[v][k] = max(max_edge[v][k - 1], max_edge[up[v][k - 1]][k - 1])


def get_max_edge(u, v):
    if depth[u] < depth[v]:
        u, v = v, u
    res = 0
    for k in reversed(range(LOG)):
        if depth[u] - depth[v] >= (1 << k):
            res = max(res, max_edge[u][k])
            u = up[u][k]
    if u == v:
        return res
    for k in reversed(range(LOG)):
        if up[u][k] != up[v][k]:
            res = max(res, max_edge[u][k], max_edge[v][k])
            u = up[u][k]
            v = up[v][k]
    return max(res, max_edge[u][0], max_edge[v][0])


Q = int(input())
for _ in range(Q):
    x, y = map(int, input().split())
    max_w = get_max_edge(x, y)
    print(total_cost - max_w)
