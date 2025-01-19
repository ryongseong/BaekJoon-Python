# https://www.acmicpc.net/problem/1268

student_num = int(input())
prev_class = []
dupli_class = [0] * student_num
for i in range(student_num):
    prev_class.append(list(map(int, input().split())))
    dupli_class[i] = [0] * student_num

for i in range(5):
    for j in range(student_num):
        for k in range(j + 1, student_num):
            if prev_class[j][i] == prev_class[k][i]:
                dupli_class[k][j] = 1
                dupli_class[j][k] = 1

cnt = []
for s in dupli_class:
    cnt.append(s.count(1))

print(cnt.index(max(cnt)) + 1)