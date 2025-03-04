N = int(input())
S = list(map(int, input().split()))

result = float("-inf")
left = 0
cnt_dict = {}
cnt = 0

for right in range(N):
    if S[right] in cnt_dict:
        cnt_dict[S[right]] += 1
    else:
        cnt_dict[S[right]] = 1
        cnt += 1

    while cnt > 2:
        cnt_dict[S[left]] -= 1
        if cnt_dict[S[left]] == 0:
            del cnt_dict[S[left]]
            cnt -= 1
        left += 1

    result = max(result, right - left + 1)

print(result)
