# https://www.acmicpc.net/problem/2863

A, B = map(int, input().split())
C, D = map(int, input().split())

value_list = [A/C + B/D, C/D + A/B, D/B + C/A, B/A + D/C]

print(value_list.index(max(value_list)))