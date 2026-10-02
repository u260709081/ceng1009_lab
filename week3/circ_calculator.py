import math

raw_input = input("Enter radius of circle to calculate circumference of: ")
try:
    radius = float(raw_input)
except ValueError:
    print(f"{raw_input} is not valid number.")
    exit(1)

circumference = 2 * math.pi * radius
print(f"Circumference of circle of radius {radius} units is {circumference} units")