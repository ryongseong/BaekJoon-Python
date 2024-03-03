paper = int(input())

board = [[0] * 100 for a in range(100)]

for a in range(paper):
    x, y = map(int, input().split())

    for i in range(x, x+10):
        for j in range(y, y+10):
            board[i][j] = 1

result = 0

for i in range(100):
    for j in range(100):
        if board[i][j] == 1:
            result += 1

print(result)

# 40분정도 해봤는데 도저히 안나와서 오픈소스의 힘을 빌렸습니다...