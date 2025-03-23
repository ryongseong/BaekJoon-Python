import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
K = int(input())
apple_points = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(K):
    x, y = map(int, input().split())
    apple_points[x][y] = 2

info = {}
L = int(input())
for _ in range(L):
    time, direct = input().split()
    info[int(time)] = direct

result = 0
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
x, y = 1, 1
apple_points[y][x] = 1
d = 0
snakes = deque([(1, 1)])

while True:
    nx, ny = x + dx[d], y + dy[d]
    if nx <= 0 or ny <= 0 or nx > N or ny > N or (nx, ny) in snakes:
        break

    if apple_points[ny][nx] != 2:
        a, b = snakes.popleft()
        apple_points[b][a] = 0

    x, y = nx, ny
    apple_points[y][x] = 1
    snakes.append((nx, ny))
    result += 1

    if result in info.keys():
        if info[result] == "D":
            d = (d + 1) % 4
        else:
            nd = 3 if d == 0 else d - 1
            d = nd

print(result + 1)
