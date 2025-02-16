import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr = list(map(int, input().split()))

start, end = 0, max(arr)

while start <= end:
    mid = (start + end) // 2
    cut = sum(max(i - mid, 0) for i in arr)
    
    if cut >= M:
        start = mid +1
    else:
        end = mid - 1

print(end)
