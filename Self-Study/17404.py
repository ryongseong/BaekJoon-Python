import sys

input = sys.stdin.readline

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

result = float("inf")
for i in range(3):
    dp = [[1001] * 3 for _ in range(n)]
    dp[0][i] = matrix[0][i]

    for j in range(1, n):
        dp[j][0] = min(dp[j - 1][1], dp[j - 1][2]) + matrix[j][0]
        dp[j][1] = min(dp[j - 1][0], dp[j - 1][2]) + matrix[j][1]
        dp[j][2] = min(dp[j - 1][0], dp[j - 1][1]) + matrix[j][2]
    dp[-1][i] = float("inf")
    result = min(result, min(dp[-1]))

print(result)
