# https://www.acmicpc.net/problem/10798

a = []

for _ in range(5):
    b= list(map(str, input().split()))
    for i in b:
        a.append(i)

print(a)