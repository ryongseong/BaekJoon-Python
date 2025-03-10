import sys

input = sys.stdin.readline

L = int(input())
S = input()

mod = 1e9 + 7
po = [0] * L
po[0] = 1
for i in range(1, L):
    po[i] = po[i - 1] * 31 % mod

low = 1
high = L - 1
answer = 0


def hash_string(length, string):
    hash = 0
    for i in range(length):
        hash *= 31
        hash %= mod
        hash += ord(string[i]) - ord("a") + 1
        hash %= mod
    return hash


def rolling_hash(hash, length, current_char, new_char):
    hash -= (ord(current_char) - ord("a") + 1) * po[length - 1]
    hash %= mod
    hash *= 31
    hash %= mod
    hash += ord(new_char) - ord("a") + 1
    hash %= mod
    return hash


while low <= high:
    mid = (low + high) // 2
    found = False
    hash = hash_string(mid, S)
    check = {}

    for i in range(0, L - mid + 1):
        if hash in check:
            for j in check[hash]:
                if S[j : j + mid] == S[i : i + mid]:
                    found = True
                    break
            check[hash].append(i)
            if found:
                break
        else:
            check[hash] = [i]

        if i + mid < L:
            hash = rolling_hash(hash, mid, S[i], S[i + mid])

    if found:
        answer = mid
        low = mid + 1
    else:
        high = mid - 1

print(answer)
