N = int(input())

rope_list = []
for _ in range(N): rope_list.append(int(input()))

rope_list.sort(reverse=True)

max_weight = 0
for i in range(N):
    max_weight = max(max_weight, rope_list[i] * (i + 1))

print(max_weight)