import turtle

# https://docs.python.org/3/library/turtle.html

print("Note that while this can take any values, only discrete squares can be drawn.")
raw_circumference = input("Enter circumference (in pixels) of square to draw: ")
try:
    circumference = float(raw_circumference)
except ValueError:
    print(f"{raw_circumference} is not valid number.")
    exit(1)

offset = (circumference / 4) / 2

# to center the square
turtle.up()
turtle.right(0)
turtle.forward(-offset)
turtle.right(-90)
turtle.forward(-offset)
turtle.down()

# actual drawing
turtle.right(0)
turtle.forward(2 * offset) # upper edge

turtle.right(90)
turtle.forward(2 * offset) # right edge

turtle.right(90)
turtle.forward(2 * offset) # bottom edge

turtle.right(90)
turtle.forward(2 * offset) # left edge

turtle.exitonclick()