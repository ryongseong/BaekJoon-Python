# https://www.acmicpc.net/problem/2675

T = int(input())

for i in range(T):
    R, S = map(str, input().split())
    for j in S:
        print(int(R) * j, end='')
    print()