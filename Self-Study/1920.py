N = int(input())
A = set(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))
for num in B:
    print(1 if num in A else 0)