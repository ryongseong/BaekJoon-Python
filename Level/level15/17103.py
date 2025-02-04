prime_list = []
check_list = [0] * 1000001
check_list[0] = 1
check_list[1] = 1

for i in range(2, 1000001):
    if check_list[i] == 0:
        prime_list.append(i)
        for j in range(2*i, 1000001, i):
            check_list[j] = 1

T = int(input())

for _ in range(T):
    cnt = 0
    N = int(input())
    for prime in prime_list:
        if prime >= N:
            break
        if not check_list[N - prime] and prime <= N - prime:
            cnt += 1
    
    print(cnt)