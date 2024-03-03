import sys

N, M = map(int, input().split())

trees = list(map(int, input().split()))

cut, high = 1, sum(trees)

while cut <= high:
    mid = (cut + high) // 2
    cnt = 0

    for tree in trees:
        if tree > mid:
            cnt += tree - mid
    
    if cnt >= M:
        cut = mid + 1
    else:
        high = mid - 1

print(high)