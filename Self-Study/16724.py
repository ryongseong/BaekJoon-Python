def sol(r, c, cnt):
    global answer
    if visited[r][c] != -1:
        if visited[r][c] == cnt:
            answer += 1
        return

    visited[r][c] = cnt
    nr, nc = r + directions[matrix[r][c]][0], c + directions[matrix[r][c]][1]
    sol(nr, nc, cnt)


directions = {"L": (0, -1), "R": (0, 1), "U": (-1, 0), "D": (1, 0)}

N, M = map(int, input().split())
matrix = [list(input()) for _ in range(N)]
visited = [[-1] * M for _ in range(N)]
answer, cnt = 0, 0

for r in range(N):
    for c in range(M):
        sol(r, c, cnt)
        cnt += 1

print(answer)
