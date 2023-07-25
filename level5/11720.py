# https://www.acmicpc.net/problem/11720

N = int(input())

M = input()

result = []
for i in M:
    result.append(int(i))

print(sum(result))