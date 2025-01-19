# # https://www.acmicpc.net/problem/3036
from fractions import Fraction
N = int(input())

first, *ring = map(int, input().split())

for i in ring:
    a = Fraction(first, i)
    print('{}/{}'.format(a.numerator, a.denominator))