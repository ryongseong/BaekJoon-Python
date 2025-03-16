directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def dfs1(r, c, tmp, cnt=1):
    global result
    if cnt == 4:
        result = max(result, tmp)
        return

    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
            visited[nr][nc] = 1
            dfs1(nr, nc, tmp + matrix[nr][nc], cnt + 1)
            visited[nr][nc] = 0


def dfs2(r, c):
    global result
    arr = []
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < M:
            arr.append(matrix[nr][nc])

    l = len(arr)
    if l == 4:
        arr.sort(reverse=True)
        arr.pop()
        result = max(result, sum(arr) + matrix[r][c])
    elif l == 3:
        result = max(result, sum(arr) + matrix[r][c])
    return


N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
result = 0
for r in range(N):
    for c in range(M):
        visited[r][c] = 1
        dfs1(r, c, matrix[r][c])
        dfs2(r, c)
        visited[r][c] = 0

print(result)
