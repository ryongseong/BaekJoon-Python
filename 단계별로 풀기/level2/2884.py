# https://www.acmicpc.net/problem/2884

hour, min = map(int, input().split())

if min < 45 :	# 분단위가 45분보다 작을 때 
    if hour == 0 :	# 0 시이면
        hour = 23
        min += 60
    else :	# 0시가 아니면 (0시보다 크면)
        hour -= 1	
        min += 60
        
print(hour, min-45)