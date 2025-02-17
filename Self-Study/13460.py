import sys
from collections import deque
input = sys.stdin.readline


directions = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1)
]


def bfs(red_r, red_c, blue_r, blue_c):
    queue = deque()
    queue.append((red_r, red_c, blue_r, blue_c))
    visited = []
    visited.append((red_r, red_c, blue_r, blue_c))
    cnt = 0
    while queue:
        for _ in range(len(queue)):
            red_r, red_c, blue_r, blue_c = queue.popleft()
            if cnt > 10:
                print(-1)
                return
            if graph[red_r][red_c] == 'O':
                print(cnt)
                return
            for dr, dc in directions:
                red_nr, red_nc = red_r, red_c
                while True:
                    red_nr += dr
                    red_nc += dc
                    if graph[red_nr][red_nc] == '#':
                        red_nr -= dr
                        red_nc -= dc
                        break
                    if graph[red_nr][red_nc] == 'O':
                        break
                blue_nr, blue_nc = blue_r, blue_c
                while True:
                    blue_nr += dr
                    blue_nc += dc
                    if graph[blue_nr][blue_nc] == '#':
                        blue_nr -= dr
                        blue_nc -= dc
                        break
                    if graph[blue_nr][blue_nc] == 'O':
                        break
                if graph[blue_nr][blue_nc] == 'O':
                    continue
                if red_nr == blue_nr and red_nc == blue_nc:
                    if abs(red_nr - red_r) + abs(red_nc - red_c) > abs(blue_nr - blue_r) + abs(blue_nc - blue_c):
                        red_nr -= dr
                        red_nc -= dc
                    else:
                        blue_nr -= dr
                        blue_nc -= dc
                if (red_nr, red_nc, blue_nr, blue_nc) not in visited:
                    queue.append((red_nr, red_nc, blue_nr, blue_nc))
                    visited.append((red_nr, red_nc, blue_nr, blue_nc))
        cnt += 1
    print(-1)

N, M = map(int, input().split())
graph = []
for r in range(N):
    graph.append(list(input()))
    for c in range(M):
        if graph[r][c] == 'R':
            red_r, red_c = r, c
        elif graph[r][c] == 'B':
            blue_r, blue_c = r, c

bfs(red_r, red_c, blue_r, blue_c)