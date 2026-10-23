import turtle

screen = turtle.Screen()
screen.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.color("lightpink")
tess.width(2)

# from exercise 1
def drawPoly(someturtle, somesides, somesize):
    outer_angle = 360 / somesides
    for _ in range(somesides):
        someturtle.forward(somesize)
        someturtle.left(outer_angle)

drawPoly(tess, 3, 50)
screen.exitonclick()