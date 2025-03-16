# https://www.acmicpc.net/problem/1712

고정비용, 가변비용, 노트북가격 = map(int, input().split())

if 가변비용>=노트북가격:
    print(-1)
else:
    print(int(고정비용/(노트북가격-가변비용)+1))