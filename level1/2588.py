# https://www.acmicpc.net/problem/2588

first = int(input())
last = int(input())

num = []
for i in reversed(str(last)):
    print(first*int(i))

print(first*last)