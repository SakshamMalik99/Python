def is_leap(year):
    leap = False
    if year % 100 == 0:
        year = year / 100
    return year % 4 == 0

    return leap


year = int(input())
print is_leap(year)
