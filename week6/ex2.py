import turtle

screen = turtle.Screen()
screen.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.color("blue")

# from exercise 1
def drawPoly(someturtle, somesides, somesize):
    outer_angle = 360 / somesides
    for _ in range(somesides):
        someturtle.forward(somesize)
        someturtle.left(outer_angle)

tess.speed(0)
for _ in range(36):
    drawPoly(tess, 4, 60)
    tess.left(10)

screen.exitonclick()    