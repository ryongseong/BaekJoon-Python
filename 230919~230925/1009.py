# https://www.acmicpc.net/problem/1009

T = int(input())

answer = []

for _ in range(T):
    a, b = map(int, input().split())

    answer.append((a**b)%10)

for i in answer:
    print(i)