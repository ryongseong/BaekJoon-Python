N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

result = 6 * N * M

for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            result -= 2
            if i > 0 and board[i-1][j] == 1:
                result -= 2
            if j > 0 and board[i][j-1] == 1:
                result -= 2

print(result)