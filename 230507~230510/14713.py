from collections import deque

parrot = int(input()) # 앵무새가 몇 마리인지 입력
sentence = [] # 빈 리스트 생성

for _ in range(parrot): 
    # 앵무새의 마리 수 만큼 반복
    sentence.append(deque(input().split()))
# 앵무새가 말하는 문장을 단어 단위로 쪼개 리스트 안에 덱 형태로 저장

result_sentence = deque(input().split())
# cseteram이 받아 적은 문장
# 문장을 단어 단위로 쪼개 덱 형태로 저장함.

def result(result_sentence, sentence):
    misscount = 0 # 이 앵무새가 아니라는 것을 확인
    birdcount = 0 # 몇 번째 앵무새인지 카운트
    isfinish = 0 # 앵무새가 말하는게 끝났는지 확인
    while result_sentence:
        # 받아적은 문장이 True일 동안
        if sentence[birdcount] and result_sentence[0] == sentence[birdcount][0]:
            # 몇 번째 앵무새인지와 받아 적은 문장의 0번 인덱스와
            # 몇 번째 앵무새의 0번 인덱스와 같다면
            sentence[birdcount].popleft()
            # 그 번호의 앵무새의 0번 인덱스 삭제
            result_sentence.popleft()
            # 받아 적은 문장의 0번 인덱스도 삭제
            misscount = 0
            # 받아적은 문장의 단어가 앵무새가 말한 단어가 있으므로 초기화
        else:
            if misscount == parrot:
                # 앵무새 중에 그 단어를 말한 앵무새가 없으면
                return False
                # False이며 종료
            misscount += 1
        birdcount = (birdcount+1)%parrot
        # 계속해서 반복문이 돌아야하기 때문에 나머지 연산자를 사용하여
        # 앵무새의 순서를 계속 돌려줌
        
    for i in range(parrot):
        if len(sentence[i]) == 0:
            isfinish += 1
        # 앵무새가 다 말했는지 검사
    
    if not result_sentence and isfinish == parrot:
    # 받아적은 문장이 다 적혔고 and 앵무새가 다 말했다면
        return True
    else:
        return False

if result(result_sentence, sentence):
    print("Possible")
else:
    print("Impossible")