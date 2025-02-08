T = int(input())

for _ in range(T):
    target = input()
    while True:
        target = target.replace('()', '', 1)
        if '()' not in target:
            break
    if target == '':
        print('YES')
    else:
        print('NO')