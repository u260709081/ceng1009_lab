def ask_input(type: str):
    try:
        raw_input = input(f"Enter {type} of rectangle: ")
        type_input = float(raw_input)
        return type_input
    except ValueError:
        print(f"Entered {type} is not a number.")
        exit(1)

width = ask_input("width")
height = ask_input("height")
area = width * height
print(f"Area of given rectangle is {area} unit^2")