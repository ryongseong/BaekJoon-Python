C, R = map(int, input().split())
K = int(input())

board = [[0] * C for _ in range(R)]
dxy = [(0, -1), (1, 0), (0, 1), (-1, 0)]

if K > C * R:
    print(0)
else:
    x, y = 0, 0
    d = 0

    for i in range(1, C * R + 1):
        if i == K:
            print(y + 1, x + 1)
            break
        board[x][y] = i
        x += dxy[d][0]
        y += dxy[d][1]

        if x < 0 or y < 0 or x >= R or y >= C or board[x][y]:
            x -= dxy[d][0]
            y -= dxy[d][1]
            d = (d + 1) % 4
            x += dxy[d][0]
            y += dxy[d][1]