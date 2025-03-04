from collections import deque


directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def bfs():
    queue = deque()
    queue.append((start_r, start_c))
    visited[start_r][start_c] = 1

    cnt = 0
    while queue:
        r, c = queue.popleft()

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if (0 <= nr < N and 0 <= nc < M) and not visited[nr][nc]:
                visited[nr][nc] = 1
                if campus[nr][nc] == "X":
                    continue
                if campus[nr][nc] == "P":
                    cnt += 1
                queue.append((nr, nc))

    return cnt if cnt else "TT"


N, M = map(int, input().split())
campus = [list(input()) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
start_r, start_c = 0, 0
for r in range(N):
    for c in range(M):
        if campus[r][c] == "I":
            start_r, start_c = r, c
            break

print(bfs())
