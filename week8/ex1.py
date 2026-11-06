def get_grade(mark: float):
    if   mark >= 90: return 'A'
    elif mark >= 80: return 'B'
    elif mark >= 70: return 'C'
    elif mark >= 60: return 'D'
    else:            return 'F'

for mark in [95,90,89.9,80,79.9,70,65,60,59.5,0]:
    print(get_grade(mark))

mark = float(input("Enter your mark: "))
print(f"Your mark of score {mark} is {get_grade(mark)}")