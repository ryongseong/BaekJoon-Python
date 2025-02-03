from math import lcm, gcd

A_first, B_first = map(int, input().split())
A_second, B_second = map(int, input().split())

분모 = lcm(B_first, B_second)

분자_A = A_first * (분모 // B_first)
분자_B = A_second * (분모 // B_second)

분자 = 분자_A + 분자_B

최대공약수 = gcd(분자, 분모)

print(f'{분자//최대공약수} {분모//최대공약수}')
