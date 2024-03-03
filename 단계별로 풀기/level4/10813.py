# https://www.acmicpc.net/problem/10813

N, M = map(int, input().split())

basket = []
for i in range(1, N+1):
    basket.append(i)

for _ in range(M):
    i, j = map(int, input().split())
    basket[i-1], basket[j-1] = basket[j-1], basket[i-1]

print(*basket)