# https://www.acmicpc.net/problem/1225

A, B = input().split()

A, B = list(map(int, A)), list(map(int, B))

print(sum(A) * sum(B))