import sys
input = sys.stdin.readline

homework = [] #과제를 리스트 형태 타입으로 설정
score = 0 #점수는 0점으로 초기값 설정

for i in range(int(input())):
    new_homework = list(map(int, input().split())) #list로 문제에 나와있는 1, A, T 설정
    if new_homework[0] == 1: #새로운 과제가 있다면
        homework.append((new_homework[1], new_homework[2])) #과제에 점수와 시간을 추가
    
    if homework:
        result, time = homework.pop() #최근 과제에서 점수와 시간을 꺼냄
        time -= 1 #시간이 지난것임으로 1 차감
        if time == 0:
            score += result #과제 시간이 0이 되면 끝낸 것이므로 점수 추가
        else:
            homework.append((result, time)) #다시 계산

print(score)