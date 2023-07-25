game, win = map(int, input().split()) # 게임 횟수, 이긴 게임을 int형으로 받고 공백을 기준으로 나눠서 game, win에 저장.
cur_rate = win*100 // game # 현재 승률

if cur_rate>=99:    # 승률이 99 이상이라면 더 해도 오르지 않음.
    print(-1)       # 냅다 -1 출력
else:
    count = 0       # count의 초깃값을 0으로 할당
    start = 1         # 1판 이상은 해야하므로 start의 초깃값 1로 할당
    end = game      # count가 게임 횟수보다 많을 수 없기에 end의 초깃값 game으로 할당
    while start <= end:           # start이 end보다 크거나 같을때까지
        search = (start+end)//2   # 추가 게임 횟수를 찾기 위해 start+end의 정수형 평균을 할당.
        if (win+search) * 100 // (game+search) <= cur_rate: # 승률에 변화가 없다면
            start = search +1     # start 값을 추가 게임 횟수에 1을 더하여 할당.
        else:                   # 승률에 변화가 있다면
            count = search      # 그 게임의 수가 최소한 해야할 게임의 수가 됨.
            end = search-1      # while문을 탈출하기 위해 추가 게임의 수의 1을 뺀 값을 end에 할당
    print(count)                # 추가 게임 수 출력