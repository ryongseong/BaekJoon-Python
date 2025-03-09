from collections import defaultdict

anagrams = defaultdict(list)
word_list = []
tmp = []

while True:
    try:
        word = input()
        word_list.append(word)
    except EOFError:
        break

for word in word_list:
    anagrams["".join(sorted(word))].append(word)

max_len = -1
for i in anagrams.keys():
    sorted_anagram = sorted(anagrams[i])
    max_len = max(max_len, len(sorted_anagram))
    tmp.append(sorted_anagram)

tmp.sort(key=lambda x: (max_len - len(x), x[0]))
for i in range(min(len(tmp), 5)):
    print(
        f'Group of size {len(tmp[i])}: {" ".join([word for word in sorted(list(set(tmp[i])))])} .'
    )
