# https://www.acmicpc.net/problem/9095

T = int(input())

dp = [0] * 12

for i in range(1, 12):
    if i == 1:
        dp[1] = 1
    elif i == 2:
        dp[2] = 2
    elif i == 3:
        dp[3] = 4
    else:
        dp[i] = dp[i-3] + dp[i-2] + dp[i-1]

for _ in range(T):
    num = int(input())
    print(dp[num])