n = int(input())

people = set()

for _ in range(n):
    name, state = input().split()

    if name not in people and state == 'enter':
        people.add(name)
    elif name in people and state == 'leave':
        people.remove(name)

people = list(people)
for person in sorted(people, reverse=True):
    print(person)
