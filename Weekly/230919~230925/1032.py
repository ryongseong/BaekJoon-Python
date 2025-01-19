# https://www.acmicpc.net/problem/1032

N = int(input())

word1 = list(input())
len_word1 = len(word1)

for _ in range(N-1):
    word2 = list(input())
    for i in range(len_word1):
        if word1[i] != word2[i]:
            word1[i] = '?'

print(''.join(word1))