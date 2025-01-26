# https://www.acmicpc.net/problem/10163
board = [[0 for _ in range(1001)] for _ in range(1001)]

n = int(input())

for i in range(1, n+1):
    x, y, w, h = map(int, input().split())
    for j in range(y, y+h):
        board[j][x:x+w] = [i]*w

for i in range(1, n+1):
    cnt = 0
    for j in range(1001):
        cnt += board[j].count(i)
    print(cnt)