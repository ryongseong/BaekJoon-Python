N = int(input())

dp = [[0] * 10 for _ in range(N)]

dp[0] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for n in range(1, N):
    dp[n][0] = dp[n-1][1]
    dp[n][9] = dp[n-1][8]

    for k in range(1, 9):
        dp[n][k] = dp[n-1][k-1] + dp[n-1][k+1]

print(sum(dp[N-1])%1000000000)