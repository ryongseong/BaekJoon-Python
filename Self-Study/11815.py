import math

N = int(input())
X = list(map(int, input().split()))

for i in X:
    root = int(math.isqrt(i))
    print(1 if root * root == i else 0, end=" ")
