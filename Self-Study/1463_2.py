import sys
from itertools import combinations

input = sys.stdin.readline

N, K = map(int, input().split())
S = input()

idx_list = []
for i in range(N):
    if S[i] != "X":
        for j in range(i + 1, N):
            if S[j] != "X" and S[i] == S[j]:
                idx_list.append((i, j))

result = 0

for i in range(1, K + 1):
    for comb in combinations(idx_list, i):
        comb = sorted(comb)
        for k in range(i - 1):
            if comb[k][1] >= comb[k + 1][0]:
                break
        else:
            cnt = sum((b - a + 1) for a, b in comb)
            result = max(result, cnt)

print(max(0, N - result))
