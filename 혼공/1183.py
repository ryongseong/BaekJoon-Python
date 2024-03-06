# https://www.acmicpc.net/problem/1183

N = int(input())
A_list = []
B_list = []

for _ in range(N):
    A, B = map(int, input().split())
    A_list.append(A)
    B_list.append(B)

for i in range(N):
    T = 0
    waiting = abs(A_list[i] + T - B_list[i])
