import heapq
import sys

input = sys.stdin.readline

N = int(input())
queue = []

for _ in range(N):
    command = int(input())
    if command == 0:
        if queue:
            print(-heapq.heappop(queue))
        else:
            print(0)
    else:
        heapq.heappush(queue, -command)