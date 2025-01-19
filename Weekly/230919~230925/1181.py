# https://www.acmicpc.net/problem/1181

N = int(input())

answer = []

for _ in range(N):
    word = input()
    answer.append(word)

answer = set(answer)
answer = list(answer)
answer.sort()
answer.sort(key=len)

for i in answer:
    print(i)