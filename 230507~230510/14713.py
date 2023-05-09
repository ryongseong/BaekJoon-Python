from collections import deque

parrot = int(input())
sentence = []

for _ in range(parrot):
    sentence.append(deque(map(str, input().split())))

result_sentence = deque(map(str, input().split()))

def result(result_sentence, n_bird):
    misscount = 0
    birdcount = 0
    isfinish = 0
    while result_sentence:
        if n_bird[birdcount] and result_sentence[0] == n_bird[birdcount][0]:
            n_bird[birdcount].popleft()
            result_sentence.popleft()
            misscount = 0
        else:
            if misscount == parrot:
                return False
            misscount += 1
        birdcount = (birdcount+1)%parrot
        
    for i in range(parrot):
        if len(n_bird[i]) == 0:
            isfinish += 1
    
    if not result_sentence and isfinish == parrot:
        return True
    else:
        return False

if result(result_sentence, sentence):
    print("Possible")
else:
    print("Impossible")

