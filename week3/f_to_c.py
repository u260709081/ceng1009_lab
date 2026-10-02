raw_input = input("Enter temperature (in fahrenheit) to convert: ")
try:
    fahr = float(raw_input)
except ValueError:
    print(f"{raw_input} is not valid number.")
    exit(1)

celc = (fahr - 32) * 5/9
print(f"{fahr} degrees fahrenheit is {celc} degrees celcius")