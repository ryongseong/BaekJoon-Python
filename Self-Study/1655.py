import heapq
import sys

input = sys.stdin.readline

N = int(input())
l_heap = []
r_heap = []

for _ in range(N):
    num = int(input())

    if len(l_heap) == len(r_heap):
        heapq.heappush(l_heap, -num)
    else:
        heapq.heappush(r_heap, num)

    if r_heap and r_heap[0] < -l_heap[0]:
        left_value = heapq.heappop(l_heap)
        right_value = heapq.heappop(r_heap)

        heapq.heappush(l_heap, -right_value)
        heapq.heappush(r_heap, -left_value)

    print(-l_heap[0])
