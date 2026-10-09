import turtle

screen = turtle.Screen()
turt = turtle.Turtle()

angles = [160, -43, 270, -97, -43, 200, -940, 17, -86]

for angle in angles:
    turt.left(angle)
    turt.forward(100)

screen.exitonclick()