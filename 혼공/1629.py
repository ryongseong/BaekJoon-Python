A, B, C = map(int, input().split())

def pow(base, exp, mod):
    if exp == 0:
        return 1
    elif exp % 2 == 0:
        return pow(base, exp // 2, mod) ** 2 % mod
    else:
        return base * pow(base, exp - 1, mod) % mod

print(pow(A, B, C))