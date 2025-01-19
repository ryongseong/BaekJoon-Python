# https://www.acmicpc.net/problem/1157

alphabet = input().upper()

alpha = list(set(alphabet))

arr = []

for i in alpha:
    count = alphabet.count(i)
    arr.append(count)

if arr.count(max(arr)) > 1:
    print("?")
else:
    max_word = arr.index(max(arr))
    print(alpha[max_word])