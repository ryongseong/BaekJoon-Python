# https://www.acmicpc.net/problem/11050
import math

N, K = map(int, input().split())

print(math.comb(N, K))