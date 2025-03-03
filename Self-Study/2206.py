from collections import deque


def bfs():
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    queue = deque([(0, 0, 0)])
    visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
    visited[0][0][0] = 1

    while queue:
        r, c, wall_break = queue.popleft()

        if (r, c) == (N - 1, M - 1):
            return visited[r][c][wall_break]

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if 0 <= nr < N and 0 <= nc < M:
                if matrix[nr][nc] == 0 and visited[nr][nc][wall_break] == 0:
                    visited[nr][nc][wall_break] = visited[r][c][wall_break] + 1
                    queue.append((nr, nc, wall_break))

                elif matrix[nr][nc] == 1 and wall_break == 0:
                    visited[nr][nc][1] = visited[r][c][wall_break] + 1
                    queue.append((nr, nc, 1))

    return -1


N, M = map(int, input().split())
matrix = [list(map(int, input())) for _ in range(N)]

print(bfs())
