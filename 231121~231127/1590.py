# https://www.acmicpc.net/problem/1590
import sys

N, T = map(int,input().split())

Bus = []
for i in range(N):
    bus = list(map(int, input().split()))

    if bus[0] <= T:
        Bus.append(bus)

for b in Bus:
    if b[0] == T:
        print(0)
        break