# K와 L값을 받음
K, L = map(int, input().split()) 

# 1차
# if K / L > L:
#     print("GOOD")
# else:
#     print("BAD",end=" ")
#     print(int(K/L))

# L보다 작은 값들 중 i로 나눴을 때 가장 작은 것이 있으면 좋지 않은 암호이므로
# 2보다 크고 L보다 작은 값들 안에서 돌림
for i in range(2, L):
    # 만약 L보다 작다면
    if K % i == 0:
    # 나쁜 암호이므로 BAD를 출력하고, K의 가장 작은 인수를 출력
        print("BAD", end=" ")
        print(i)
    # for문 탈출
        exit()

# L보다 작은 값이 없다면 그 L이 좋은 암호이므로 GOOD 출력
print("GOOD")