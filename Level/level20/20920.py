import sys
input = sys.stdin.readline

N, M = map(int, input().split())

word_dict = {}

for _ in range(N):
    word = input().strip()
    if len(word) < M:
        continue

    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1

word_dict = sorted(word_dict.items(), key = lambda x: (-x[1], -len(x[0]), x[0]))

for i in word_dict:
    print(i[0])