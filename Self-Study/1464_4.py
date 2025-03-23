import sys

input = sys.stdin.readline


def sol():
    two_or_more_lst = [p for p in metion_list if p >= 2]
    avg = sum(two_or_more_lst) / len(two_or_more_lst) if two_or_more_lst else 0

    diff = [0] * (M + 1)
    over_avg_cnt = 0

    for p in metion_list:
        if p <= avg:
            if p > M:
                print(-1)
                return
            diff[0] += 1
            diff[p] -= 1
        else:
            over_avg_cnt += 1

    counts = [0] * M
    counts[0] = diff[0]
    for i in range(1, M):
        counts[i] = counts[i - 1] + diff[i]
    counts[0] += over_avg_cnt

    print(" ".join(map(str, counts)))


N, M = map(int, input().split())
metion_list = list(map(int, input().split()))
sol()
