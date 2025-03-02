from collections import deque

directions = [(1, 2), (2, 1), (1, -2), (2, -1), (-1, 2), (-2, 1), (-1, -2), (-2, -1)]


def bfs():
    queue = deque()
    queue.append((start_r, start_c))

    while queue:
        r, c = queue.popleft()
        if (r, c) == (end_r, end_c):
            return matrix[r][c] - 1
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < I and 0 <= nc < I and matrix[nr][nc] == 0:
                matrix[nr][nc] = matrix[r][c] + 1
                queue.append((nr, nc))


T = int(input())

for _ in range(T):
    I = int(input())
    matrix = [[0 for _ in range(I)] for _ in range(I)]
    start_r, start_c = map(int, input().split())
    end_r, end_c = map(int, input().split())
    matrix[start_r][start_c] = 1
    print(bfs())
