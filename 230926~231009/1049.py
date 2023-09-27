# https://www.acmicpc.net/problem/1049

# multi는 6개 묶음

N, M = map(int, input().split())

multi_list = []
single_list = []

for _ in range(M):
    multi, single = map(int, input().split())
    multi_list.append(multi)
    single_list.append(single)

multi_list.sort()
single_list.sort()

if multi_list[0] <= single_list[0]*6:
    answer = multi_list[0] * (N // 6) + single_list[0] * (N % 6)
    if single_list[0] * (N % 6) > multi_list[0]:
        answer = multi_list[0] * (N // 6 + 1)
else:
    answer = single_list[0] * N

print(answer)