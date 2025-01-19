N = input()

if "0" not in N:
    print(-1)
else:
    num_sum = 0
    for i in range(len(N)):
        num_sum += int(N[i])
    
    if num_sum % 3 != 0:
        print(-1)
    else:
        for i in sorted(N, reverse=True):
            print(i, end="")
        print()