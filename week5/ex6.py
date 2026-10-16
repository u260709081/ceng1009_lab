import turtle

screen = turtle.Screen()
drawer = turtle.Turtle()

screen.bgcolor("lightgreen")
drawer.color("lightpink")

drawer.penup()
drawer.backward(60)
drawer.pensize(7)

for _ in range(5):
    drawer.pendown()
    for _ in range(4):
        drawer.forward(20)
        drawer.left(90)
    drawer.penup()
    drawer.forward(20+20)

screen.exitonclick()