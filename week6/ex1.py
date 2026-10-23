import turtle

screen = turtle.Screen()
screen.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.color("lightpink")
tess.width(2)

def drawPoly(someturtle, somesides, somesize):
    outer_angle = 360 / somesides
    for _ in range(somesides):
        someturtle.forward(somesize)
        someturtle.left(outer_angle)

drawPoly(tess, 8, 50)
screen.exitonclick()