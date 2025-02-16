N = int(input())
dp = [1] * N

arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort()

for i in range(1, N):
    for j in range(i):
        if arr[j][1] < arr[i][1]:
            dp[i] = max(dp[i], dp[j]+1)

print(N-max(dp))