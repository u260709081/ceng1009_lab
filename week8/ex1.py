def get_grade(mark: float):
    if   mark >= 90: return 'A'
    elif mark >= 80: return 'B'
    elif mark >= 70: return 'C'
    elif mark >= 60: return 'D'
    else:            return 'F'

print(get_grade(79.9999))
print(get_grade(80))
print(get_grade(91))
print(get_grade(50))