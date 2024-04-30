# https://www.acmicpc.net/problem/2161

N = int(input())

cards = [i for i in range(1, N+1)]

while len(cards) > 1:
    print(cards.pop(0), end=' ')
    cards.append(cards.pop(0))

print(cards.pop(0))