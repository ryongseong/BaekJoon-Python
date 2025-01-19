# https://www.acmicpc.net/problem/4963

from collections import deque
import sys
input = sys.stdin.readline

d = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]


def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(8):
            nx = x + d[i][0]
            ny = y + d[i][1]
            if 0 <= nx < h and 0 <= ny < w:
                if arr[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
    return 1


while True:
    w, h = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(h)]
    result = 0
    visited = [[0] * (w) for _ in range(h)]
    if w == 0 and h == 0:
        break
    for x in range(h):
        for y in range(w):
            if arr[x][y] == 1 and not visited[x][y]:
                result += bfs(x, y)
    print(result)