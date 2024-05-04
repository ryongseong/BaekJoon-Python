# https://www.acmicpc.net/problem/1427

num = int(input())

lst = []
for i in str(num):
    lst.append(int(i))

lst.sort(reverse=True)

for i in lst:
    print(i, end="")