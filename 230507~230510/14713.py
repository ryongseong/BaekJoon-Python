from collections import deque

parrot = int(input())
word = []

for _ in range(parrot):
    word.append(deque(map(str, input().split())))
sentence = deque(map(str, input().split()))

def result(sentence, n_bird):
    misscount = 0
    birdcount = 0
    isfinish = 0
    while sentence:
        if n_bird[birdcount] and sentence[0] == n_bird[birdcount][0]:
            n_bird[birdcount].popleft()
            sentence.popleft()
            misscount = 0
        else:
            if misscount == parrot:
                return False
            misscount += 1
        birdcount = (birdcount+1)%parrot
        
    for i in range(parrot):
        if len(n_bird[i]) == 0:
            isfinish += 1
    
    if not sentence and isfinish == parrot:
        return True
    else:
        return False

if result(sentence, word):
    print("Possible")
else:
    print("Impossible")

