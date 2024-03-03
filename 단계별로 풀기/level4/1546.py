# https://www.acmicpc.net/problem/1546

N = int(input())

scores = list(map(int, input().split()))

high = max(scores)

result = []
for i in scores:
    result.append(i/high*100)

score = sum(result)/N
print(score)