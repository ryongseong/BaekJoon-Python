# https://www.acmicpc.net/problem/1183
# Not Finished yet

N = int(input())

time_list = []

for _ in range(N):
    A_i, B_i = map(int, input().split())
    time_list.append((A_i + B_i) / 2)
