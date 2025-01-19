# https://www.acmicpc.net/problem/1978

N = int(input())

numbers = map(int, input().split())

count = 0

for i in numbers:
    err = 0
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                err += 1
        if err == 0:
            count += 1

print(count)