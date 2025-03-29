gugudan = set()

for i in range(1, 10):
    for j in range(1, 10):
        gugudan.add(i * j)

print(1 if int(input()) in gugudan else 0)
