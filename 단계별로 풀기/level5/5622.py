# https://www.acmicpc.net/problem/5622

dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

number = input()
count = 0

for j in range(len(number)):
    for i in dial:
        if number[j] in i:
            count += dial.index(i)+3

print(count)