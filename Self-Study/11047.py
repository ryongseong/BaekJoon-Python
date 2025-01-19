# https://www.acmicpc.net/problem/11047

N, K = map(int, input().split())

coin = []

for _ in range(N):
    coin.append(int(input()))

coin.sort(reverse=True)
count = 0
for i in coin:
    if K >= i:
        count += K // i
        K %= i
        if K <= 0:
            break

print(count)