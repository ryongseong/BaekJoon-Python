import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
li = list(map(int, input().split()))
li = li[::-1]

dq = deque()
for i in range(N):
    if li[i] == 1:
        dq.appendleft(i + 1)
    elif li[i] == 2:
        dq.insert(1, i + 1)
    elif li[i] == 3:
        dq.append(i + 1)

print(*dq)
