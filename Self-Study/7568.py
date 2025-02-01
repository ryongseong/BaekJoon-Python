N = int(input())

student_list = []

for _ in range(N):
    x, y = map(int, input().split())
    student_list.append((x, y))

for student in student_list:
    rank = 1
    for other_student in student_list:
        if student[0] < other_student[0] and student[1] < other_student[1]:
            rank += 1
    print(rank, end=' ')