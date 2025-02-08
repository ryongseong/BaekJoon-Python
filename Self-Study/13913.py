from collections import deque

def path(x):
    lst = []
    for _ in range(times[x] + 1):
        lst.append(x)
        x = move_lst[x]
    print(*lst[::-1])

def bfs():
    queue = deque([N])
    while queue:
        x = queue.popleft()
        if x == K:
            print(times[x])
            path(x)
            return
        for i in (x-1, x+1, 2*x):
            if 0 <= i < 100001 and not times[i]:
                times[i] = times[x] + 1
                move_lst[i] = x
                queue.append(i)

N, K = map(int, input().split())
times = [0] * 100001
move_lst = [0] * 100001
bfs()