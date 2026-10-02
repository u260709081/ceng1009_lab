raw_year = input("Enter your birth year to calculate your age: ")
try:
    year = int(raw_year)
except ValueError:
    print(f"{raw_year} is not valid integer.")
    exit(1)

# shouldn't i use 2026 here? i was told to use 2024 in lab pdf 
age = 2024 - year
print(f"You are {age} years old.")