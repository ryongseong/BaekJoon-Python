def is_leap(year):
    if year % 4 != 0:
        return False
    r = year % 400
    if r in (100, 200, 300):
        return False
    return True


def days_in_month(year, month):
    if month in (1, 3, 5, 7, 8, 10, 12):
        return 31
    if month in (4, 6, 9, 11):
        return 30
    if month == 2:
        return 29 if is_leap(year) else 28


def convert_to_year(Y, M, D, h, m, s):
    sec = 0
    for month in range(1, M):
        sec += days_in_month(Y, month) * 86400
    sec += (D - 1) * 86400 + h * 3600 + m * 60 + s
    total = sum(days_in_month(Y, month) * 86400 for month in range(1, 13))
    return Y + sec / total


def convert_to_month(Y, M, D, h, m, s):
    full_months = (Y - 1) * 12 + (M - 1)
    sec = (D - 1) * 86400 + h * 3600 + m * 60 + s
    total = days_in_month(Y, M) * 86400
    return full_months + sec / total


def convert_to_day(Y, M, D, h, m, s):
    leaps = (Y - 1) // 4 - (Y - 1) // 100 + (Y - 1) // 400
    days_before = (Y - 1) * 365 + leaps
    days_in_current_year = sum(days_in_month(Y, month) for month in range(1, M))
    days_total = days_before + days_in_current_year + (D - 1)
    sec_fraction = (h * 3600 + m * 60 + s) / 86400
    return days_total + sec_fraction


T = int(input())
for _ in range(T):
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    option = input().strip()

    if option == "Year":
        birth_val = convert_to_year(*a)
        current_val = convert_to_year(*b)
    elif option == "Month":
        birth_val = convert_to_month(*a)
        current_val = convert_to_month(*b)
    elif option == "Day":
        birth_val = convert_to_day(*a)
        current_val = convert_to_day(*b)

    result = int(current_val - birth_val)
    print(result)
