N, M = map(int, input().split())

no_listen_people = {input() for _ in range(N)}

result = set()
for _ in range(M):
    name = input()
    if name in no_listen_people:
        result.add(name)

result = list(result)
print(len(result))

for person in sorted(result):
    print(person)