N, M = map(int, input().split())
data = list(map(int, input().split()))

cnt = 0
left, right = 0, 0
sum_v = 0

while right < N:
    sum_v += data[right]

    while sum_v > M and left <= right:
        sum_v -= data[left]
        left += 1

    if sum_v == M:
        cnt += 1

    right += 1

print(cnt)
