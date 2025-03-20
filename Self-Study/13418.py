from sys import stdin

input = stdin.readline


def kruskal(N, edges):
    w_cost, b_cost = 0, N
    max_parent = [i for i in range(N + 1)]
    min_parent = [i for i in range(N + 1)]

    def find(parent, n):
        if parent[n] != n:
            parent[n] = find(parent, parent[n])
        return parent[n]

    def union(parent, a, b):
        a = find(parent, a)
        b = find(parent, b)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b

    for n1, n2, w in edges:
        if w == 1:
            if find(min_parent, n1) != find(min_parent, n2):
                union(min_parent, n1, n2)
                b_cost -= 1
        else:
            if find(max_parent, n1) != find(max_parent, n2):
                union(max_parent, n1, n2)
                w_cost += 1

    return w_cost**2 - b_cost**2


N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M + 1)]

print(kruskal(N, edges))
