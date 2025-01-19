while True:
    k, *S = map(int,input().split())
    if k == 0 : break

    for i in range(k-5):
        for j in range(i+1,k-4):
            for l in range(j+1,k-3):
                for m in range(l+1,k-2):
                    for n in range(m+1,k-1):
                        for o in range(n+1,k):
                            print(S[i],S[j],S[l],S[m],S[n],S[o])

    print()