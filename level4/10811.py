# https://www.acmicpc.net/problem/10811

N, M = map(int, input().split())

basket = []
for i in range(1, N+1):
    basket.append(i)

for _ in range(M):
    i, j = map(int, input().split())
    action = basket[i-1: j]
    action.reverse()
    basket[i-1: j] = action

print(*basket)