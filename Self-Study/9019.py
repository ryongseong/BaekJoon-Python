import sys
from collections import deque

input = sys.stdin.readline


def bfs():
    visited = [0] * 10001
    queue = deque([[A, ""]])
    visited[A] = 1

    while queue:
        num, command = queue.popleft()

        if num == B:
            print(command)
            return

        D = num * 2 % 10000
        if not visited[D]:
            visited[D] = 1
            queue.append([D, command + "D"])

        S = (num - 1) % 10000
        if not visited[S]:
            visited[S] = 1
            queue.append([S, command + "S"])

        L = (num % 1000) * 10 + num // 1000
        if not visited[L]:
            visited[L] = 1
            queue.append([L, command + "L"])

        R = (num % 10) * 1000 + num // 10
        if not visited[R]:
            visited[R] = 1
            queue.append([R, command + "R"])


for _ in range(int(input())):
    A, B = map(int, input().split())

    bfs()
