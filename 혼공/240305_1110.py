# https://www.acmicpc.net/problem/1110

N = input()

if int(N) < 10:
    N = "0" + N

first_value = int(N) // 10
second_value = int(N) % 10
count = 0

while True:
    first_value, second_value = str(first_value), str(second_value)
    count += 1
    if second_value + str((int(first_value) + int(second_value)) % 10) == str(N):
        break;
    second_memories_value = second_value
    second_value = (int(first_value) + int(second_value)) % 10
    first_value = second_memories_value

print(count)