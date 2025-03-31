import sys
from collections import deque

imput = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

dir = ((0, 1), (0, -1), (1, 0), (-1, 0))

edge = set()


def condition(ni, nj):
    return ni < 0 or ni >= n or nj < 0 or nj >= m


def marking(y, x, mark):
    q = deque()
    q.append((y, x))
    graph[y][x] = mark
    visited[y][x] = 1
    while q:
        i, j = q.popleft()
        for dy, dx in dir:
            ni, nj = i + dy, j + dx
            if condition(ni, nj) or not graph[ni][nj] or visited[ni][nj]:
                continue
            graph[ni][nj] = mark
            visited[ni][nj] = 1
            q.append((ni, nj))


def getDist(y, x, now):
    q = deque()
    for idx in range(4):
        q.append((y, x, 0, dir[idx]))
    while q:
        i, j, cnt, nowDir = q.popleft()
        if graph[i][j] != 0 and graph[i][j] != now:
            if cnt > 2:
                edge.add((cnt - 1, now, graph[i][j]))
            continue
        ni, nj = i + nowDir[0], j + nowDir[1]
        if condition(ni, nj) or graph[ni][nj] == now:
            continue
        q.append((ni, nj, cnt + 1, nowDir))


mark = 1
for i in range(n):
    for j in range(m):
        if graph[i][j] and not visited[i][j]:
            marking(i, j, mark)
            mark += 1


for i in range(n):
    for j in range(m):
        if graph[i][j] != 0:
            visited = [[0] * m for _ in range(n)]
            getDist(i, j, graph[i][j])

edge = list(edge)
edge.sort()


def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)
    if a > b:
        parent[b] = a
    else:
        parent[a] = b


parent = [i for i in range(mark)]

result = 0

num = 0
for cost, a, b in edge:
    if find(a) != find(b):
        num += 1
        union(a, b)
        result += cost

if result == 0 or num != mark - 2:
    print(-1)
else:
    print(result)
