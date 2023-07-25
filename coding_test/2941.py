# https://www.acmicpc.net/problem/2941

cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

alpha = input()

for i in cro:
    alpha = alpha.replace(i, '*')

print(len(alpha))