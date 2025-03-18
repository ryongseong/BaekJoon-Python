N = int(input())
loads = list(map(int, input().split()))
prices = list(map(int, input().split()))

min_price = float("inf")
result = 0

for i in range(N - 1):
    min_price = min(min_price, prices[i])
    result += min_price * loads[i]

print(result)
