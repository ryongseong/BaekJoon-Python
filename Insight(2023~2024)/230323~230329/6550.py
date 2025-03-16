import sys
input = sys.stdin.readline

while True:

    sentence1, sentence2 = input().split()

    correct = 0 # 몇개의 부분 문자열인지
    answer = 0 # 정답 초기값 설정

    for i in range(len(sentence2)):
        if sentence2[i] == sentence1[correct]: #1번째 문장을 부분화 시켜 2번째 문장과 대조했을 때 같다면
            correct += 1 # 부분 문자열의 수 1 올림
            if correct == len(sentence1): # 부분 문자열의 수가 1번째 문장의 길이와 같다면
                answer = 1 # 정답처리
                break

    if answer == 1 : 
        print("Yes")
    else:
        print("No")
