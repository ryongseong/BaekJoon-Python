dp = [0] * (101)
dp[0] = 1
dp[1] = 0
dp[2] = 2
for n in range(3, 101):
    dp[n] = dp[n - 1] + 2 * dp[n - 2]

for _ in range(int(input())):
    n = int(input())
    print(dp[n])
