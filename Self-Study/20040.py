import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        return find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)

    if rank[a] > rank[b]:
        parent[b] = a
    elif rank[a] < rank[b]:
        parent[a] = b
    else:
        parent[b] = a
        rank[a] += 1

def sol():
    for i in range(m):
        a, b = map(int, input().split())
        if find(a) == find(b):
            return i + 1
        union(a, b)
    return 0

n, m = map(int, input().split())
parent = [i for i in range(n)]
rank = [0 for _ in range(n)]
print(sol())