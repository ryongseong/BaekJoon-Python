# https://www.acmicpc.net/problem/2566

numbers = [list(map(int, input().split())) for _ in range(9)]

max_number = 0
row, col = 0, 0

for i in range(9):
    for j in range(9):
        if max_number <= numbers[i][j]:
            row = i + 1
            col = j + 1
            max_number = numbers[i][j]
        
print(max_number)
print(row, col)