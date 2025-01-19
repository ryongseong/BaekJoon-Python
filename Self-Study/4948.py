prime_list = [2]

for i in range(3, 123456 * 2 + 1, 2):
    for j in prime_list:
        if i % j == 0:
            break
        if j ** 2 > i:
            prime_list.append(i)
            break

while True:
    n = int(input())
    if n == 0: break
    cnt = 0
    for i in prime_list:
        if n < i <= n * 2:
            cnt += 1
    print(cnt)