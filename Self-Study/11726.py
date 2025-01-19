# https://www.acmicpc.net/problem/11726

dp = [0] * 1001

dp[1] = 1
dp[2] = 2

for i in range(3, 1001):
    dp[i] = dp[i - 1] + dp[i - 2]

N = int(input())

print(dp[N] % 10007)