# https://www.acmicpc.net/problem/1434

N, M = map(int, input().split())
box = list(map(int, input().split()))
book_list = list(map(int, input().split()))

idx = 0
for book in book_list:
    while True:
        if book <= box[idx]:
            box[idx] -= book
            break

        idx += 1

print(sum(box))