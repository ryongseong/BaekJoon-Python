# https://www.acmicpc.net/problem/1541

식 = input().split('-')
result = 0

for i in 식[0].split('+'): result += int(i)

for i in 식[1:]:
    for j in i.split('+'):
        result -= int(j)

print(result)