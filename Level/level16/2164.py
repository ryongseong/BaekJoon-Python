import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
queue = deque([i for i in range(1, N+1)])

Flag = 1

while True:
    if len(queue) == 1:
        print(queue[0])
        break
    
    if Flag:
        queue.popleft()
        Flag = Flag ^ 1
    else:
        queue.append(queue.popleft())
        Flag = Flag ^ 1