T = int(input())

for _ in range(T):
    N = int(input())
    dic = {}
    for _ in range(N):
        name, kind = input().split()
        if kind not in dic:
            dic[kind] = 1
        else:
            dic[kind] += 1
    result = 1
    for value in dic.values():
        result *= (value + 1)
    print(result - 1)