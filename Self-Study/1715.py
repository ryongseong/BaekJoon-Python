import heapq

N = int(input())
cards = []
for _ in range(N):
    heapq.heappush(cards, int(input()))

result = 0
while len(cards) > 1:
    a = heapq.heappop(cards)
    b = heapq.heappop(cards)
    sum_v = a + b
    result += sum_v
    heapq.heappush(cards, sum_v)

print(result)