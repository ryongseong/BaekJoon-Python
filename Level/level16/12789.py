N = int(input())

numbers = list(map(int, input().split()))

waiting = []

now_number = 1

while True:
    if numbers and numbers[0] == now_number:
        numbers.pop(0)
        now_number += 1
    elif waiting and waiting[-1] == now_number:
        waiting.pop()
        now_number += 1
    elif numbers:
        waiting.append(numbers.pop(0))
    else:
        break

print("Sad" if waiting else "Nice")