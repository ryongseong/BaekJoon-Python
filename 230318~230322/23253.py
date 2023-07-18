import sys
input = sys.stdin.readline

n, m = map(int, input().split()) # 책의 개수인 n과 더미의 개수인 m을 정해줌
result = True # 정리가 잘 된 것을 초기 값으로 설정

for i in range(m):
    a = int(input()) # 더미 안에 몇 개의 책이 들어가는지 정해줌
    b = list(map(int, input().split())) # 위에서 정해진 책의 개수대로 밑에서 부터 책의 번호를 설정
    for j in range(a-1):
        if b[j] < b[j+1]: 
            result = False # 만약 더미에서 아래의 책이 위의 책보다 번호가 낮다면 순서가 틀리기 때문에 정리가 안된것으로 함.
            break
    if not result:
        break # 그렇지 않다면 result값을 초기 값대로 해줌

print('Yes' if result else 'No') # result값을 가지고 정리가 잘 되어있다, 안되어있다 출력