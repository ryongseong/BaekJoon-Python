from collections import deque

n, k = map(int, input().split())

game = deque([])

for i in range(1, n + 1):
    game.append(i)

print('<', end='')

while game:
    for i in range(k-1):
        game.append(game[0])
        game.popleft()
    print(game.popleft(), end='')
    if game:
        print(', ', end='')

print('>')