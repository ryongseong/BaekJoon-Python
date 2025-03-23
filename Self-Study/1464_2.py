def sol():
    global B
    for item in buy_list:
        B -= item_dict[item]
        if B < 0:
            return False
    return True


B, N, M = map(int, input().split())
item_dict = {}
for _ in range(N):
    name, price = input().split()
    item_dict[name] = int(price)

buy_list = [input() for _ in range(M)]

print("acceptable" if sol() else "unacceptable")
