def calculate_distance(star_1, star_2):
    return ((star_1[0] - star_2[0]) ** 2 + (star_1[1] - star_2[1]) ** 2) ** 0.5


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


n = int(input())
parents = [i for i in range(n + 1)]
stars = [list(map(float, input().split())) for _ in range(n)]
edges = []
cost = 0

for i in range(n - 1):
    for j in range(i + 1, n):
        edges.append((calculate_distance(stars[i], stars[j]), i, j))

edges.sort()

for edge in edges:
    c, x, y = edge

    if find(x) != find(y):
        union(x, y)
        cost += c


print(round(cost, 2))
