import sys

N, M = map(int, sys.stdin.readline().split())

pocketmon_dict = {}
number_dict = {}

for i in range(1, N+1):
    pocketmon = sys.stdin.readline().strip() # 시간 초과를 위한 strip() 사용
    pocketmon_dict[pocketmon] = i
    number_dict[i] = pocketmon

for _ in range(M):
    q = sys.stdin.readline().strip() # 시간 초과를 위한 strip() 사용
    if q.isdigit():
        print(number_dict[int(q)])
    else:
        print(pocketmon_dict[q])