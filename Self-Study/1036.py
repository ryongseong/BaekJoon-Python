N = int(input())
word_list = [input() for _ in range(N)]
K = int(input())

num36 = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
num36_diff = []
num_sum = 0
num_sep = []

for word in word_list:
    temp = [c for c in word]
    num_sep.append(temp)
    num_sum += int(word, 36)

for k in num36:
    num_sum_diff = 0
    for num in num_sep:
        temp_str = ''
        for n in num:
            if n == k:
                temp_str += 'Z'
            else:
                temp_str += n
        num_sum_diff += int(temp_str, 36)
    num36_diff.append(num_sum_diff - num_sum)

max_sum = num_sum + sum(sorted(num36_diff, reverse=True)[:K])

result = ''
while max_sum:
    result = num36[max_sum % 36] + result
    max_sum //= 36

print(result if result else '0')