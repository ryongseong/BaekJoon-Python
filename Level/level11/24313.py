a1, a0 = map(int, input().split())
c = int(input())
n = int(input())

flag = True
for i in range(n, 101):
    if (a1 * i + a0) > (i * c):
        flag = False
        break

print(int(flag))