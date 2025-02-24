import sys

S = input()
q = int(sys.stdin.readline())

prefix = {chr(i): [0] * (len(S) + 1) for i in range(97, 123)}

for i, char in enumerate(S):
    for key in prefix:
        prefix[key][i + 1] = prefix[key][i] + (1 if key == char else 0)

for _ in range(q):
    c, l, r = sys.stdin.readline().split()
    l, r = int(l), int(r)
    print(prefix[c][r + 1] - prefix[c][l])