import sys
input = sys.stdin.readline

n = int(input())

arr = [int(input()) for _ in range(n)]

if n == 1:
    print(arr[0])
    exit()
elif n == 2:
    print(sum(arr[:2]))
    exit()

dp = [0] * (n+1)
dp[0] = arr[0]
dp[1] = arr[0] + arr[1]
dp[2] = max(arr[2] + arr[0], arr[2]+arr[1], dp[1])

for i in range(3, n):
    dp[i] = max(arr[i]+dp[i-2], arr[i]+arr[i-1]+dp[i-3], dp[i-1])

print(max(dp))
