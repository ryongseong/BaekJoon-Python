import sys

input = sys.stdin.readline

game, win = map(int, input().split()) # 게임 횟수, 이긴 게임을 int형으로 받고 공백을 기준으로 나눠서 X, Y에 저장.
cur_rate = win*100 // game

count = 0 # 카운트 초기값 0

while (win+count)*100//(game+count) <= cur_rate:
    if game == win: # 게임 횟수와 이긴 횟수가 같다면
        count = -1 # 더이상 변화가 있을 수 없으므로 count에 -1을 할당.
        break
    count += 1


print(count) # 몇 판을 더 해야하는지 출력