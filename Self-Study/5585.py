remain_money = 1000 - int(input())
cnt = 0
coins = [500, 100, 50, 10, 5, 1]

for coin in coins:
    cnt += remain_money // coin
    remain_money %= coin

print(cnt)