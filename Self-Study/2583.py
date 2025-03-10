from collections import deque

m, n, k = map(int, input().split())
graph = [[0] * n for _ in range(m)]
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(m - y1 - 1, m - y2 - 1, -1):
            graph[j][i] = 1

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def bfs(x, y):
    global answer
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 1
    size = 1
    while queue:
        x, y = queue.popleft()
        for dr, dc in directions:
            nx, ny = x + dr, y + dc
            if 0 <= nx < m and 0 <= ny < n and graph[nx][ny] == 0:
                graph[nx][ny] = 1
                queue.append((nx, ny))
                size += 1
    result.append(size)


result = []
for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            bfs(i, j)

result.sort()
print(len(result))
for i in result:
    print(i, end=" ")
