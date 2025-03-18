from collections import deque

n, k = map(int, input().split())
game = deque([i for i in range(1, n + 1)])

print("<", end="")

while game:
    for i in range(k - 1):
        game.append(game.popleft())
    print(game.popleft(), end="")
    if game:
        print(", ", end="")

print(">")
