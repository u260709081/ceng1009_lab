days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

for (i, day) in enumerate(days):
    print(f"{i} = {day}")

raw_start = input("Enter your starting day: ")
try:
    start = int(raw_start)
    day = days[start]
except ValueError:
    print(f"{raw_start} is not valid number.")
    exit(1)
except IndexError:
    print(f"Please pick one of valid days.")
    exit(1)

raw_length = input("Enter amount of days you have as vacation: ")
try:
    length = int(raw_length)
except ValueError:
    print(f"{raw_length} is not valid integer.")
    exit(1)

end_day = (start + length) % 7
print(f"Your vacation ends at {end_day}")