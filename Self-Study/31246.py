import sys

input = sys.stdin.readline

N, K = map(int, input().split())
arr = []

for _ in range(N):
    A, B = map(int, input().split())
    arr.append(B - A)

arr.sort()

print(0 if arr[K - 1] < 0 else arr[K - 1])
