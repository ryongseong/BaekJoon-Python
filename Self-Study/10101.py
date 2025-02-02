first = int(input())
second = int(input())
third = int(input())

if first + second + third != 180:
    print('Error')
else:
    if first == second and second == third:
        print('Equilateral')
    elif first == second or second == third or first == third:
        print('Isosceles')
    else:
        print('Scalene')