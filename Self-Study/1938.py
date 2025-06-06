import sys
from collections import deque

input = sys.stdin.readline


def find_start_end_coordinate():
    for y in range(n):
        for x in range(n):
            if graph[y][x] == "B":
                if x < n - 1 and graph[y][x + 1] == "B":
                    sy = y
                    sx = x + 1
                    graph[y][x] = graph[y][x + 1] = graph[y][x + 2] = "0"
                    sf = 1
                elif y < n - 1 and graph[y + 1][x] == "B":
                    sy = y + 1
                    sx = x
                    graph[y][x] = graph[y + 1][x] = graph[y + 2][x] = "0"
                    sf = 2
            elif graph[y][x] == "E":
                if x < n - 1 and graph[y][x + 1] == "E":
                    ey = y
                    ex = x + 1
                    graph[y][x] = graph[y][x + 1] = graph[y][x + 2] = "0"
                    ef = 1
                elif y < n - 1 and graph[y + 1][x] == "E":
                    ey = y + 1
                    ex = x
                    graph[y][x] = graph[y + 1][x] = graph[y + 2][x] = "0"
                    ef = 2

    return sy, sx, sf, ey, ex, ef


def can_it_go(y, x, flag, rotation=False):
    if rotation:
        flag = (0, 2, 1)[flag]
        if visited[y][x] & flag:
            return False
        if x == 0 or x == n - 1 or y == 0 or y == n - 1:
            return False  # 범위를 넘어가면 안 됨
        if sum([int(i) for r in range(y - 1, y + 2) for i in graph[r][x - 1 : x + 2]]):
            return False
    else:
        if visited[y][x] & flag:
            return False
        else:
            if flag == 1:
                if x == 0 or x == n - 1:
                    return False
                if graph[y][x - 1] or graph[y][x + 1]:
                    return False
            elif flag == 2:
                if y == 0 or y == n - 1:
                    return False
                if graph[y - 1][x] or graph[y + 1][x]:
                    return False

    return True


def bfs(queue):
    cnt = 0
    dir = [[1, 0], [-1, 0], [0, 1], [0, -1], [0, 0]]
    while queue:
        cnt += 1
        for _ in range(len(queue)):
            y, x, flag = queue.popleft()
            for dy, dx in dir:
                ny, nx = y + dy, x + dx
                if 0 <= ny < n and 0 <= nx < n and graph[ny][nx] == 0:
                    rotation = not (dy | dx)
                    if can_it_go(ny, nx, flag, rotation=rotation):
                        flag = (3 ^ flag) if rotation else flag
                        if (ny, nx, flag) == (ey, ex, ef):
                            return cnt
                        else:
                            visited[ny][nx] |= flag
                            queue.append((ny, nx, flag))

    return 0


n = int(input())
graph = [list(input().strip()) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

sy, sx, sf, ey, ex, ef = find_start_end_coordinate()
graph = [list(map(int, row[:])) for row in graph]

queue = deque()
queue.append((sy, sx, sf))

print(bfs(queue))
