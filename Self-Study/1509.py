import sys

input = sys.stdin.readline

S = input().strip()
n = len(S)
palindrome = [[0] * n for _ in range(n)]
dp = [2500] * (n + 1)
dp[-1] = 0
for i in range(n):
    for j in range(i + 1):
        if S[j] == S[i] and (i - j < 2 or palindrome[j + 1][i - 1]):
            palindrome[j][i] = 1
            dp[i] = min(dp[i], dp[j - 1] + 1)

print(dp[n - 1])
