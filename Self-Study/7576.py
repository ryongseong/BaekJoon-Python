from collections import deque

M, N = map(int, input().split())

tomato_list = [list(map(int, input().split())) for _ in range(N)]

queue = deque([])
for i in range(N):
    for j in range(M):
        if tomato_list[i][j] == 1:
            queue.append((i, j))

d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

while queue:
    x, y = queue.popleft()

    for dx, dy in d:
        nx, ny = x + dx, y + dy

        if 0 <= nx < N and 0 <= ny < M and tomato_list[nx][ny] == 0:
            tomato_list[nx][ny] = tomato_list[x][y] + 1
            queue.append((nx, ny))

result = 0
for i in range(N):
    for j in range(M):
        if tomato_list[i][j] == 0:
            print(-1)
            exit()
        result = max(result, tomato_list[i][j])

print(result - 1)