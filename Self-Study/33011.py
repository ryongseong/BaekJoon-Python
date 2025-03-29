def solve_game(test_cases):
    for N, A in test_cases:
        odd = sum(1 for x in A if x % 2 == 1)
        even = N - odd

        odd_cw, even_cw = odd - 1, even
        turn = 1
        cw_first = "odd"
        winner = None
        while True:
            if turn % 2 == 1:
                if cw_first == "odd":
                    if even_cw == 0:
                        winner = "amsminn"
                        break
                    even_cw -= 1
                else:
                    if odd_cw == 0:
                        winner = "amsminn"
                        break
                    odd_cw -= 1
            else:
                if cw_first == "odd":
                    if odd_cw == 0:
                        winner = "heeda0528"
                        break
                    odd_cw -= 1
                else:
                    if even_cw == 0:
                        winner = "heeda0528"
                        break
                    even_cw -= 1
            turn += 1

        odd_cw, even_cw = odd, even - 1
        turn = 1
        cw_first = "even"
        winner2 = None
        while True:
            if turn % 2 == 1:
                if cw_first == "odd":
                    if even_cw == 0:
                        winner2 = "amsminn"
                        break
                    even_cw -= 1
                else:
                    if odd_cw == 0:
                        winner2 = "amsminn"
                        break
                    odd_cw -= 1
            else:
                if cw_first == "odd":
                    if odd_cw == 0:
                        winner2 = "heeda0528"
                        break
                    odd_cw -= 1
                else:
                    if even_cw == 0:
                        winner2 = "heeda0528"
                        break
                    even_cw -= 1
            turn += 1

        if winner == "amsminn" or winner2 == "amsminn":
            print("amsminn")
        else:
            print("heeda0528")


T = int(input())
test_cases = []
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    test_cases.append((N, A))

solve_game(test_cases)
