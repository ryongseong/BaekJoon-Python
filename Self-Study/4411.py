while True:
    n = int(input())
    if n == 0:
        break
    money_list = [float(input()) for _ in range(n)]
    avg_money = sum(money_list) / n
    result1 = sum(
        filter(lambda x: x > 0, [round(avg_money - i, 2) for i in money_list])
    )
    result2 = sum(
        filter(lambda x: x > 0, [round(i - avg_money, 2) for i in money_list])
    )

    print(f"${min(result1, result2):.2f}")
