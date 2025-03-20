def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]


def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parents[b] = a
    else:
        parents[a] = b


N = int(input())
M = int(input())
parents = [i for i in range(N + 1)]
edegs = [list(map(int, input().split())) for _ in range(M)]
edegs.sort(key=lambda x: x[2])
cost = 0

for i in range(M):
    a, b, c = edegs[i]
    if find(a) != find(b):
        union(a, b)
        cost += c

print(cost)
