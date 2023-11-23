# https://www.acmicpc.net/problem/1590

버스의개수, 터미널도착시간 = map(int, input().split())
버스정보 = []
for _ in range(버스의개수):
    버스시작, 간격, 대수 = map(int, input().split())
    시간표 = [버스시작+간격*i for i in range(대수)]
    if 시간표[-1] < 터미널도착시간:
        continue
    시작, 끝 = 0, 대수-1
    시작2 = 0
    while 시작 <= 끝:
        중앙 = (시작+끝)//2
        if 시간표[중앙] >= 터미널도착시간:
            시작2 = 중앙
            끝 = 중앙-1
        else:
            시작 = 중앙+1
    버스정보.append(시간표[시작2]-터미널도착시간)
print(min(버스정보) if 버스정보 else -1)