from collections import deque

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def bfs(r, c):
    queue.append((r, c))
    visited[r][c] = 1
    while queue:
        r, c = queue.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if (
                0 <= nr < N
                and 0 <= nc < N
                and matrix[nr][nc] == matrix[r][c]
                and not visited[nr][nc]
            ):
                visited[nr][nc] = 1
                queue.append((nr, nc))


N = int(input())
matrix = [list(input()) for _ in range(N)]
queue = deque()
normal_cnt = 0
danger_cnt = 0

visited = [[0 for _ in range(N)] for _ in range(N)]
for r in range(N):
    for c in range(N):
        if not visited[r][c]:
            bfs(r, c)
            normal_cnt += 1

visited = [[0 for _ in range(N)] for _ in range(N)]
for r in range(N):
    for c in range(N):
        if matrix[r][c] == "G":
            matrix[r][c] = "R"

for r in range(N):
    for c in range(N):
        if not visited[r][c]:
            bfs(r, c)
            danger_cnt += 1

print(normal_cnt, danger_cnt)
