# https://www.acmicpc.net/problem/2559
import sys

input = sys.stdin.readline

N, K = map(int, input().split())

temp = list(map(int, input().split()))

result = []
result.append(sum(temp[:K]))

for i in range(N - K):
    result.append(result[i] - temp[i] + temp[K+i])

print(max(result))