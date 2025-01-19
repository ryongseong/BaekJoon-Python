# https://www.acmicpc.net/problem/15552
import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    case = list(map(int,input().rstrip().split()))
    case_list = case[0] + case[1]
    print(case_list)