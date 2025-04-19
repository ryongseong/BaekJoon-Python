import sys
input = sys.stdin.readline

for _ in range(int(input())):
    a, b = map(int, input().split())
    print(1 if b % a == 0 and b // a >= 2 else 0)
