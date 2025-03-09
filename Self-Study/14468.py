words = input()
result = 0

for s in range(52):
    for e in range(s + 1, 52):
        if words[s] == words[e]:
            cows = words[s : e + 1]
            for i in cows:
                if cows.count(i) == 1:
                    result += 1
            break

print(result // 2)
