# https://www.acmicpc.net/problem/2346
from collections import deque

N = int(input())

balloons = deque(enumerate(map(int, input().split())))
result = []

while balloons:
    idx, balloon = balloons.popleft()
    result.append(idx+1)

    if balloon > 0:
        balloons.rotate(-(balloon -1))
    elif balloon < 0:
        balloons.rotate(-balloon)

print(' '.join(map(str, result)))