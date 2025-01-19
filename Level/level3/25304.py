# https://www.acmicpc.net/problem/25304

X = int(input())
N = int(input())

for i in range(N):
    a, b = map(int,input().split())
    cost = a * b
    X -= cost

if X == 0:
    print("Yes")
else:
    print("No")