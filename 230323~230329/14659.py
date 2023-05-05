import sys
input = sys.stdin.readline

people = int(input())
person = list(map(int, input().split()))

highest = 0 # 가장 높은 봉우리(초기 값)
cnt = 0 # 잡은 수(초기 값)
result =[] # 잡은 수들 리스트에 넣기위한 초기값

for i in person: 
    if i > highest: # 사람들의 높이를 비교함 (만약 i번째 값이 가장 높은 값보다 높은 경우)
        highest = i # 가장 높은 봉우리의 값이 변경
        cnt = 0 # 그로인해 잡은 수는 초기화
    else:
        cnt += 1 # 봉우리가 가장 높기 때문에 계속해서 잡은 수를 증가시킴
    result.append(cnt) # 높이 비교해서 초기화 될때마다 리스트에 잡은 수를 추가 시킴

print(max(result)) # 리스트에서 가장 높은 수를 찾으면 답