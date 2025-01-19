# https://www.acmicpc.net/problem/1063

from collections import deque

n, k = map(int, input().split())

game = deque([])

for i in range(0, n):
    game.append(i+1)

print('<', end='')

while game:
    for i in range(k-1):
        game.append(game[0])
        game.popleft()
    print(game.popleft(), end='')
    if game:
        print(', ', end='')

print('>')