# https://www.acmicpc.net/problem/2908

a, b = input().split()

a = a[::-1]
b = b[::-1]

print(max(int(a), int(b)))