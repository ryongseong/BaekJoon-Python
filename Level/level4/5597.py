# https://www.acmicpc.net/problem/5597

student = []
for i in range(1, 31):
    student.append(i)

for _ in range(28):
    hw = int(input())
    student.remove(hw)

print(min(student))
print(max(student))