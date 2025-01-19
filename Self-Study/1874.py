# https://www.acmicpc.net/problem/1874

n = int(input())
arr = []
answer = []
confirm = 0
count = 1

for _ in range(n):
    num = int(input())
    while count <= num:
        arr.append(count)
        answer.append("+")
        count += 1

    if arr[-1] == num:
        arr.pop()
        answer.append("-")
    else:
        confirm = 1

if confirm == 0:
    for i in answer:
        print(i)
elif confirm == 1:
    print("NO")