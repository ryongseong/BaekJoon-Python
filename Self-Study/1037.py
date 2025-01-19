# https://www.acmicpc.net/problem/1037

N = int(input())

divisor = list(set(map(int, input().split())))

print(max(divisor) * min(divisor))