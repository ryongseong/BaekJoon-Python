# https://www.acmicpc.net/problem/2798

# 카드 개수 N장과 합인 M을 입력받음.
N, M = map(int, input().split())
# 카드 입력
cards = list(map(int, input().split()))

# 합의 결과의 초깃값 0 할당.
result = 0

# 3장을 뽑아야하기에 N장에서 2장을 뺀 것에서 돌림
for i in range(N-2):
# 1장을 뽑았고 2장 남았기에 1장을 뺀 것에서 돌림    
    for j in range(i+1, N-1):
# 1장 남았기에 N까지 돌림
        for k in range(j+1, N):
# M보다 크면 안되기에 계속 돌림
            if cards[i] + cards[j] + cards[k] > M:
                continue
            else:
# M보다 작은 값들 중 i번째, j번째, k번째의 카드의 합 중 최댓값을 result에 할당
                result = max(result, cards[i] + cards[j] + cards[k])

# 결과 출력
print(result)