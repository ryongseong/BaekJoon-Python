# https://www.acmicpc.net/problem/10798

result = []
length = []

for _ in range(5):
    word = input()
    result.append(word)
    length.append(len(word))

answer = ''
for i in range(max(length)):
    for j in range(5):
        if i < length[j]:
            answer += result[j][i]

print(answer)