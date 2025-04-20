import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
time = 0
direction = [(-1, 0), (1, 0), (0, 1), (0, -1)]


def melt():
    decrease = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if matrix[i][j] > 0:
                for dx, dy in direction:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < n and 0 <= nj < m and matrix[ni][nj] == 0:
                        decrease[i][j] += 1

    for i in range(n):
        for j in range(m):
            matrix[i][j] = max(matrix[i][j] - decrease[i][j], 0)


def count_icebergs():
    visited = [[False] * m for _ in range(n)]
    cnt = 0

    for i in range(n):
        for j in range(m):
            if matrix[i][j] > 0 and not visited[i][j]:
                cnt += 1
                q = deque([(i, j)])
                visited[i][j] = True
                while q:
                    x, y = q.popleft()
                    for dx, dy in direction:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < n and 0 <= ny < m:
                            if matrix[nx][ny] > 0 and not visited[nx][ny]:
                                visited[nx][ny] = True
                                q.append((nx, ny))
    return cnt


while True:
    count = count_icebergs()

    if count >= 2:
        print(time)
        break
    elif count == 0:
        print(0)
        break

    melt()
    time += 1
