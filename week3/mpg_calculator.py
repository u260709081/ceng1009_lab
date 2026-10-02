def ask_input(type: str):
    try:
        raw_input = input(f"Enter {type} to calculate MPG: ")
        type_input = float(raw_input)
        return type_input
    except ValueError:
        print(f"Entered {type} is not a number.")
        exit(1)

miles = ask_input("miles")
gallons = ask_input("gallons")
mpg = miles/gallons

print(f"MPG of car is {mpg} miles per gallon")