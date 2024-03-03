# https://www.acmicpc.net/problem/1297
import math

D, H, W = map(int, input().split())

R = D/math.sqrt((H**2+W**2))

print(int(H*R), int(W*R))