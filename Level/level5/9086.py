# https://www.acmicpc.net/problem/9086

T = int(input())

for i in range(T):
    alpha = input()
    if len(alpha) < 2:
        print(alpha*2)
    else:
        print(alpha[0]+alpha[-1])