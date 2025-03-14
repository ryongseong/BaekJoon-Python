import sys

input = sys.stdin.readline

A = [""] + list(input().strip())
B = [""] + list(input().strip())
dp = [[""] * (len(B)) for _ in range(len(A))]

for i in range(1, len(A)):
    for j in range(1, len(B)):
        if A[i] == B[j]:
            dp[i][j] = dp[i - 1][j - 1] + A[i]
        else:
            if len(dp[i - 1][j]) >= len(dp[i][j - 1]):
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i][j - 1]


print(len(dp[-1][-1]))
print(dp[-1][-1])
