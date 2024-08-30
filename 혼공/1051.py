# https://www.acmicpc.net/problem/1051

N, M = map(int, input().split())
board = [list(map(int, input().rstrip())) for _ in range(N)]
answer = 1

for i in range(N):
    for j in range(M):
        for k in range(1, min(N-i, M-j)):
            if board[i][j] == board[i+k][j] == board[i][j+k] == board[i+k][j+k]:
                answer = max(answer, k+1)

print(answer**2)