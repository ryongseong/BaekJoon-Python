# https://www.acmicpc.net/problem/2852

def convertSecToMinSec(s):
    m = s // 60
    s = s % 60
    m = '0' + str(m) if m < 10 else str(m)
    s = '0' + str(s) if s < 10 else str(s)
    return m + ':' + s

def convertMinSecToSec(m, s):
    return m * 60 + s

n = int(input())

one_time = 0
two_time = 0
flag = 0
end_time = convertMinSecToSec(48, 0)

for i in range(n):
    team, time = input().split()
    m, s=map(int, time.split(':'))
    time = convertMinSecToSec(m, s)
    if team == '1':
        if flag == 0:
            one_time += end_time - time
        flag += 1
        if flag == 0:
            if two_time > 0:
                two_time -= end_time - time
    else: 
        if flag == 0:
            two_time += end_time - time
        flag -= 1
        if flag == 0:
            if one_time > 0:
                one_time -= end_time - time


print(convertSecToMinSec(one_time))
print(convertSecToMinSec(two_time))