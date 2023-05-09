from collections import deque

aengmubird = int(input())
sentence = deque(map(str, input().split()))
word = []

for _ in range(aengmubird):
    word.append(deque(str, input().split()))

wordscount = 0
wordcount = 0

