from math import sqrt

A, B = map(int, input().split())

is_prime = [True for _ in range(B+1)]
is_prime[1] = False

cnt = 0
for i in range(2, B+1):
    if not is_prime[i]:
        continue
    
    for j in range(i**2, B+1, i):
        is_prime[j] = False

def find(n):
    cnt = 0
    for i in range(2, int(sqrt(n) + 1)):
        while n % i == 0:
            cnt += 1
            n //= i
    if n != 1:
        cnt += 1
    return cnt

for i in range(A, B+1):
    if is_prime[find(i)] == True: cnt += 1

print(cnt)