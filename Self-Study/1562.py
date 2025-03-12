import sys

input = sys.stdin.readline

n = int(input())
bit_range = 1 << 10
M = 10**9

dp = [[[0] * bit_range for _ in range(10)] for _ in range(n + 1)]

for i in range(10):
    dp[1][i][1 << i] = 1

for i in range(1, n):
    for j in range(10):
        for k in range(bit_range):
            if 0 <= j < 9:
                a = k | 1 << (j + 1)
                dp[i + 1][j + 1][a] += dp[i][j][k]
                dp[i + 1][j + 1][a] %= M
            if 0 < j <= 9:
                a = k | 1 << (j - 1)
                dp[i + 1][j - 1][a] += dp[i][j][k]
                dp[i + 1][j - 1][a] %= M

result = 0
for i in range(1, 10):
    result += dp[n][i][0b1111111111]
    result %= M

print(result)
