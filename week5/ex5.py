import turtle

screen = turtle.Screen()
drawer = turtle.Turtle()

length = 100

for _ in range(5):
    drawer.forward(length)
    drawer.right(144)

screen.exitonclick()