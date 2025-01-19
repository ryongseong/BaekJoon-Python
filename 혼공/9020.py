T = int(input())

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

for _ in range(T):
    n = int(input())

    for i in range(n // 2, 1, -1):
        if is_prime(i) and is_prime(n - i):
            print(i, n - i)
            break