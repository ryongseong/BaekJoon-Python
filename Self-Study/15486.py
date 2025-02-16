import sys

N = int(sys.stdin.readline().rstrip())

time_table = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]

dp = [0] * (N+1)

for i in range(1, N+1):
    dp[i] = max(dp[i], dp[i -1])
    day = i + time_table[i-1][0] - 1
    if day <= N:
        dp[day] = max(dp[day], dp[i-1] + time_table[i-1][1])

print(max(dp))