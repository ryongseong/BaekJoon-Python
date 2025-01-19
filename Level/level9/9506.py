# https://www.acmicpc.net/problem/9506

while True:
    number = int(input())

    if number == -1:
        break

    number_low = []

    for i in range(1, number):
        if number % i == 0:
            number_low.append(i)

    if sum(number_low) == number:
        print(number, '=', ' + '.join(str(x) for x in number_low))
    else:
        print(number,'is NOT perfect.')