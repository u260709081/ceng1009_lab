import turtle

sides = int(input("How many sides? "))
side_color = input("What color for sides? ")
poly_color = input("What color for polygon? ")

screen = turtle.Screen()
turt = turtle.Turtle()

outer_angle = 360 / sides
turt.color(side_color)
turt.fillcolor(poly_color)
turt.begin_fill()
for _ in range(sides):
    turt.forward(100)
    turt.left(outer_angle)
turt.end_fill()

screen.exitonclick()