import sys

input = sys.stdin.readline

for _ in range(int(input())):
    N, K = map(int, input().split())
    # print((N // (2**K)) - (N // (2 ** (K + 1))))
    print((N >> K) - (N >> (K + 1)))
