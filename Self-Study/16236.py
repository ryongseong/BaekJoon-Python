import sys
from collections import deque

input = sys.stdin.readline


def bfs(x, y):
    visited = [[0] * N for _ in range(N)]
    queue = deque([[x, y]])
    cand = []

    visited[x][y] = 1

    while queue:
        i, j = queue.popleft()

        for dx, dy in directions:
            nx, ny = i + dx, j + dy

            if 0 <= nx and nx < N and 0 <= ny and ny < N and visited[nx][ny] == 0:
                if space[x][y] > space[nx][ny] and space[nx][ny] != 0:
                    visited[nx][ny] = visited[i][j] + 1
                    cand.append((visited[nx][ny] - 1, nx, ny))
                elif space[x][y] == space[nx][ny]:
                    visited[nx][ny] = visited[i][j] + 1
                    queue.append([nx, ny])
                elif space[nx][ny] == 0:
                    visited[nx][ny] = visited[i][j] + 1
                    queue.append([nx, ny])

    return sorted(cand, key=lambda x: (x[0], x[1], x[2]))


N = int(input())
space = [list(map(int, input().split())) for _ in range(N)]

directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

pos = []
for i in range(N):
    for j in range(N):
        if space[i][j] == 9:
            pos.append(i)
            pos.append(j)

cnt = 0
i, j = pos
size = [2, 0]

while True:
    space[i][j] = size[0]
    cand = deque(bfs(i, j))

    if not cand:
        break

    step, xx, yy = cand.popleft()
    cnt += step
    size[1] += 1

    if size[0] == size[1]:
        size[0] += 1
        size[1] = 0

    space[i][j] = 0
    i, j = xx, yy

print(cnt)
