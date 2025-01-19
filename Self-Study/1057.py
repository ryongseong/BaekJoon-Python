# https://www.acmicpc.net/problem/1057

N, K, L = map(int, input().split())

rounds = 0

while K != L:
    K = (K + 1) // 2
    L = (L + 1) // 2
    rounds += 1

print(rounds)