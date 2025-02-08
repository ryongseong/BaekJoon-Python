N = int(input())

matrix = [list(map(int, input())) for _ in range(N)]

d = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0)
]

def dfs(x, y):
    global cnt
    matrix[x][y] = 0
    cnt += 1
    for dx, dy in d:
        if 0 <= (x + dx) < N and 0 <= (y + dy) < N:
            if matrix[x + dx][y + dy] == 1:
                dfs(x + dx, y + dy)

result = []
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 1:
            cnt = 0
            dfs(i, j)
            result.append(cnt)

print(len(result))
for i in sorted(result):
    print(i)