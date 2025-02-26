import sys
from collections import deque

input = sys.stdin.readline


def bfs(r, c):
    global cnt
    queue = deque()
    queue.append((r, c))
    sink_matrix[r][c] = True
    cnt += 1

    while queue:
        x, y = queue.popleft()
        for dr, dc in directions:
            nr = x + dr
            nc = y + dc
            if not (0 <= nr < N and 0 <= nc < N) or sink_matrix[nr][nc]:
                continue
            sink_matrix[nr][nc] = True
            queue.append((nr, nc))


N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
max_rain = float("-inf")
for r in range(N):
    for c in range(N):
        max_rain = max(max_rain, matrix[r][c])

directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

result_list = []

for rain in range(max_rain):
    cnt = 0
    sink_matrix = [[False for _ in range(N)] for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if matrix[r][c] <= rain:
                sink_matrix[r][c] = True

    for r in range(N):
        for c in range(N):
            if not sink_matrix[r][c]:
                bfs(r, c)

    result_list.append(cnt)

print(max(result_list))
