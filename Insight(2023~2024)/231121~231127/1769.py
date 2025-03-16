# https://www.acmicpc.net/problem/1769 

큰자연수 = input()

변환횟수 = 0
while int(큰자연수) >= 10:
    변환수 = 0
    for 자릿수 in range(len(큰자연수)):
        변환수 += int(큰자연수[자릿수])
    변환횟수 += 1
    큰자연수 = str(변환수)

print(변환횟수)
print("YES" if int(큰자연수)%3 == 0 else "NO")