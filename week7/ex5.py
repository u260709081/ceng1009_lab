import turtle

screen = turtle.Screen()
tess = turtle.Turtle()
tess.shape("triangle")

def fancySquare(t: turtle.Turtle):
    for _ in range(4):
        t.stamp()
        t.forward(50)
        t.right(90)

fancySquare(tess)
screen.exitonclick()