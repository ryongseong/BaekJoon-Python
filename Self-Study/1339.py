import sys
input = sys.stdin.readline

N = int(input())

arr = [input().strip() for _ in range(N)]
words = {}
for s in arr:
    x = len(s) - 1
    for i in s:
        if i in words:
            words[i] += 10**x
        else:
            words[i] = 10**x
        x -= 1

sorted_words = sorted(words.values(), reverse=True)
result = 0
num = 9
for k in sorted_words:
    result += k * num
    num -= 1
print(result)
