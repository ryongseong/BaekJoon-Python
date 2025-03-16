import sys
from collections import deque

input = sys.stdin.readline


def bfs():
    queue = deque([1])
    matrix[1] = 0
    cnt = 0

    while queue:
        l = len(queue)
        for _ in range(l):
            idx = queue.popleft()

            if idx == 100:
                print(cnt)
                break

            for i in range(1, 7):
                n_idx = idx + i

                if n_idx <= 100 and not matrix[n_idx]:
                    matrix[n_idx] = 1

                    if n_idx in ladders.keys():
                        matrix[ladders[n_idx]] = 1
                        queue.append(ladders[n_idx])

                    elif n_idx in snakes.keys():
                        matrix[snakes[n_idx]] = 1
                        queue.append(snakes[n_idx])
                    else:
                        queue.append(n_idx)
        cnt += 1


N, M = map(int, input().split())
matrix = [0] * 101

ladders = {}
for _ in range(N):
    x, y = map(int, input().split())
    ladders[x] = y

snakes = {}
for _ in range(M):
    x, y = map(int, input().split())
    snakes[x] = y

bfs()
