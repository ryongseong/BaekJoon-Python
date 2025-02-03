N = int(input())

member_list = []

for _ in range(N):
    age, name = input().split()
    member_list.append((int(age), name))

member_list.sort(key=lambda x: x[0])

for member in member_list:
    print(member[0], member[1])