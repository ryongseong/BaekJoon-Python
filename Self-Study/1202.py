import sys
import heapq

input = sys.stdin.readline

N, K = map(int, input().split())

jewels = [tuple(map(int, input().split())) for _ in range(N)]
jewels.sort(key=lambda x: x[0])

bags = [int(input()) for _ in range(K)]
bags.sort()

result = 0
heap = []
jewel_idx = 0

for bag in bags:
    while jewel_idx < N and jewels[jewel_idx][0] <= bag:
        heapq.heappush(heap, -jewels[jewel_idx][1])
        jewel_idx += 1
    if heap:
        result -= heapq.heappop(heap)

print(result)
