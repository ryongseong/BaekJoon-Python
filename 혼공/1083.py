# https://www.acmicpc.net/problem/1083
N = int(input())
arr = list(map(int, input().split()))
S = int(input())

n = len(arr)
for i in range(n-1, 0, -1):
    for j in range(i):
        if (arr[j] < arr[j+1]):
            arr[j], arr[j+1] = arr[j+1], arr[j]
            S -= 1
        if S <= 0:
            break

print(*arr)