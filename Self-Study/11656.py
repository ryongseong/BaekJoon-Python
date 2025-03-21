S = input()
for s in sorted(S[i:] for i in reversed(range(len(S)))):
    print(s)
