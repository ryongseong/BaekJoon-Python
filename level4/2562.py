# https://www.acmicpc.net/problem/2562

num = []
for i in range(1,10):
    num.append(int(input()))

print(max(num))
print(num.index(max(num))+1)