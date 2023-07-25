# https://www.acmicpc.net/problem/11022

T = int(input())

for i in range(1, T+1):
    A, B = map(int,input().split())
    result = A + B
    print("Case #{}: {} + {} = {}".format(i, A, B, result))