import sys
import heapq
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    max_heap, min_heap = [], []
    visited = [False] * 1000001
    k = int(input())

    for n in range(k):
        a, b = input().split()
        if a == 'I':
            heapq.heappush(min_heap, (int(b), n))
            heapq.heappush(max_heap, (-int(b), n))
            visited[n] = True
        elif a == 'D':
            if b == '-1':
                while min_heap and not visited[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                if min_heap:
                    visited[min_heap[0][1]] = False
                    heapq.heappop(min_heap)
            elif b == '1':
                while max_heap and not visited[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                if max_heap:
                    visited[max_heap[0][1]] = False
                    heapq.heappop(max_heap)
    
    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop(min_heap)
    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap)
    
    if min_heap and max_heap:
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print("EMPTY")