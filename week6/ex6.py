import turtle

screen = turtle.Screen()
tess = turtle.Turtle()
tess.speed(0)

def drawSprite(someturtle, somesides, somelength):
    angle = 360 / somesides

    for _ in range(somesides):
        someturtle.forward(somelength)
        someturtle.backward(somelength)
        someturtle.left(angle)

drawSprite(tess, 15, 120)
screen.exitonclick()