# https://www.acmicpc.net/problem/1100 

chess_board = [[1, 0, 1, 0, 1, 0, 1, 0],
               [0, 1, 0, 1, 0, 1, 0, 1],
               [1, 0, 1, 0, 1, 0, 1, 0],
               [0, 1, 0, 1, 0, 1, 0, 1],
               [1, 0, 1, 0, 1, 0, 1, 0],
               [0, 1, 0, 1, 0, 1, 0, 1],
               [1, 0, 1, 0, 1, 0, 1, 0],
               [0, 1, 0, 1, 0, 1, 0, 1]]

check_board = []

for i in range(8):
    check_board.append(list(input()))

count = 0
for i in range(8):
    for j in range(8):
        if check_board[i][j] == 'F' and chess_board[i][j] == 1:
            count += 1

print(count)