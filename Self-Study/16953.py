A, B = map(int, input().split())
r = 1
flag = True
while B != A:
    r += 1
    temp = B
    if B % 10 == 1:
        B //= 10
    elif B % 2 == 0:
        B //= 2

    if temp == B:
        flag = False
        break

print(r if flag else -1)