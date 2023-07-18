n, x = map(int, input().split()) # 맵 사용하는 방법을 잘 몰라서 검색해서 풀었습니다...

number = list(map(int, input().split()))

for i in number:
    if i < x:
        print(i, end = ' ')
