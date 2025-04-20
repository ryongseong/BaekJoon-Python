# N = int(input())
# data = list(map(str, range(1, N + 1)))
# result_dict = {str(i): 0 for i in range(10)}


# for num in data:
#     for n in num:
#         result_dict[n] += 1

# for v in result_dict.values():
#     print(v, end=" ")


def count_digits(N):
    count = [0] * 10
    digit = 1
    start = 1
    end = N

    while start <= end:
        while end % 10 != 9 and start <= end:
            for d in str(end):
                count[int(d)] += digit
            end -= 1

        while start % 10 != 0 and start <= end:
            for d in str(start):
                count[int(d)] += digit
            start += 1

        if start > end:
            break

        num_blocks = end // 10 - start // 10 + 1
        for i in range(10):
            count[i] += num_blocks * digit

        start //= 10
        end //= 10
        digit *= 10

    return count


N = int(input())
result = count_digits(N)
print(*result)
