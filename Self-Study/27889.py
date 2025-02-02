def full_name(short_name):
    if short_name == 'NLCS':
        return 'North London Collegiate School'
    elif short_name == 'BHA':
        return 'Branksome Hall Asia'
    elif short_name == 'KIS':
        return 'Korea International School'
    elif short_name == 'SJA':
        return 'St. Johnsbury Academy'

print(full_name(input()))