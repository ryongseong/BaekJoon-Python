# https://www.acmicpc.net/problem/1244

def change(number):
    if switchStatus[number] == 0:
        switchStatus[number] = 1
    else:
        switchStatus[number] = 0
    return

switchNum = int(input())
switchStatus = [float('inf')]+list(map(int, input().split()))
studentNum = int(input())

for i in range(studentNum):
    gender, number = map(int, input().split())

    if gender == 1:
        for i in range(number, switchNum+1, number):
            change(i)
    else:
        change(number)
        for k in range(switchNum//2):
            if number + k > switchNum or number - k < 1:
                break
            if switchStatus[number+k] == switchStatus[number-k]:
                change(number+k)
                change(number-k)
            else:
                break

for i in range(1,switchNum+1):
    print(switchStatus[i], end=' ')
    if i % 20 == 0:
        print()