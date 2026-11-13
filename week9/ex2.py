def is_leap_year(year: int):
    if year % 400 == 0: return True
    if year % 100 == 0: return False
    if year % 4 == 0: return True
    return False


print(is_leap_year(2026))
print(is_leap_year(2027))
print(is_leap_year(2028))
print(is_leap_year(2029))
