# https://www.acmicpc.net/problem/10952

while True:
    A, B = map(int,input().split())
    if A != 0:
        if B != 0:
            result = A + B
            print(result)
    elif A == 0:
        if B == 0:
            break