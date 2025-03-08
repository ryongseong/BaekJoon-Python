N = int(input())

plus_list = []
minus_list = []
result = 0

for _ in range(N):
    num = int(input())
    if num > 1:
        plus_list.append(num)
    elif num < 1:
        minus_list.append(num)
    else:
        result += num

plus_list.sort(reverse=True)
minus_list.sort()

if len(plus_list) % 2 == 1:
    plus_list.append(1)
if len(minus_list) % 2 == 1:
    minus_list.append(1)

for i in range(0, len(plus_list), 2):
    result += plus_list[i] * plus_list[i + 1]
for i in range(0, len(minus_list), 2):
    result += minus_list[i] * minus_list[i + 1]

print(result)
