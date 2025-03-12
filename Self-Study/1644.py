import sys
import math

input = sys.stdin.readline


def dfs(x):
    global Y
    global matched
    global visited
    if visited[Y.index(x)]:
        return False
    visited[Y.index(x)] = True
    for y in Y:
        if x + y in primes:
            if y not in matched or dfs(matched[y]):
                matched[y] = x
                return True
    return False


def get_prime_list():
    primes = []
    for i in range(2, 2000):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
        else:
            continue
    return primes


N = int(input())
X = list(map(int, input().split()))

primes = get_prime_list()

answers = []
for i in X:
    matched = {}
    if i == X[0]:
        continue
    if X[0] + i in primes:
        if N == 2:
            answers.append(i)
            break
        Y = [x for x in X]
        del Y[0]
        del Y[Y.index(i)]
        matched = {}
        for y in Y:
            visited = [False for _ in range(len(Y))]
            dfs(y)

    if N != 2 and len(matched) == N - 2:
        answers.append(i)

if not answers:
    answers.append(-1)

answers.sort()

print(" ".join(list(map(str, answers))))
