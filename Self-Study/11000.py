import sys
import heapq
input = sys.stdin.readline

N = int(input())
time = [list(map(int, input().split())) for _ in range(N)]
time.sort(key=lambda x: (x[0], x[1]))

heap = [time[0][1]]
for i in range(1, N):
    if heap[0] <= time[i][0]:
        heapq.heappop(heap)
    heapq.heappush(heap, time[i][1])

print(len(heap))