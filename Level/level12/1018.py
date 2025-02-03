# https://www.acmicpc.net/problem/1018

N, M = map(int, input().split())
chess_board = []
result = []

for _ in range(N):
    chess_board.append(input())

for i in range(N-7):
    for j in range(M-7):
        white = 0
        black = 0

        for k in range(i, i+8):
            for l in range(j, j + 8):
                if (k + l) % 2 == 0:
                    if chess_board[k][l] == 'B': white += 1
                    if chess_board[k][l] == 'W': black += 1
                else:
                    if chess_board[k][l] == 'W': white += 1
                    if chess_board[k][l] == 'B': black += 1
        
        result.append(min(white, black))

print(min(result))