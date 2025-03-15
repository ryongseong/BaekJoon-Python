def sol():
    for i in range(n - 1):
        if phone_list[i] in phone_list[i + 1][0 : len(phone_list[i])]:
            return False
    return True


for _ in range(int(input())):
    n = int(input())
    phone_list = [input() for _ in range(n)]
    phone_list.sort()
    print("YES" if sol() else "NO")
