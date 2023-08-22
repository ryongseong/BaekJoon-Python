# https://www.acmicpc.net/problem/2292

N = int(input())

first = 1
count = 1

while N > first :
    first += 6 * count
    count += 1

print(count)