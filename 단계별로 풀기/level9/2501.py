# https://www.acmicpc.net/problem/2501

N, K = map(int, input().split())

result = []

for i in range(1, int(N**(1/2)) + 1):
        if (N % i == 0):
            result.append(i) 
            if ( (i**2) != N): 
                result.append(N // i)

result.sort()

try:
    print(result[K-1])
except:
    print(0)