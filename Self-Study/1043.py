n, m = map(int, input().split())
knows = set(input().split()[1:])
party = []

for _ in range(m):
    party.append(set(input().split()[1:]))

for _ in range(m):
    for p in party:
        if p & knows:
            knows = knows.union(p)

cnt = 0
for p in party:
    if p & knows:
        continue
    cnt += 1

print(cnt)
