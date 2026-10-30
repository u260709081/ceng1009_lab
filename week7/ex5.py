import turtle

screen = turtle.Screen()
tess = turtle.Turtle()
#tess.shape("triangle")

def drawSprite(t: turtle.Turtle, legs: int, length: int):
    angle = 360 / legs
    for _ in range(legs):
        t.forward(length)
        t.backward(length)
        t.right(angle)

def fancySquare(t: turtle.Turtle):
    for _ in range(4):
        drawSprite(t, 5, 20)
        #t.stamp()
        t.forward(50)
        t.right(90)

fancySquare(tess)
screen.exitonclick()