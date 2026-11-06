import turtle

screen = turtle.Screen()
tess = turtle.Turtle()

screen.bgcolor("lightgreen")
tess.color("blue")
tess.width(2)

bars = [48, 117, 200, 240, 160, 260, 220]

BAR_WIDTH = 30

def drawBar(t: turtle.Turtle, height: int):
    t.left(90)

    t.color("blue")
    t.begin_fill()
    t.forward(height)
    t.right(90)

    t.color("red")
    t.write(height)

    t.color("blue")
    t.forward(BAR_WIDTH)
    t.right(90)
    t.forward(height)

    if height >= 200:
        t.color("red")
    elif height >= 100:
        t.color("yellow")
    else:
        t.color("green")
    t.end_fill()
    t.left(90)

for bar in bars:
    drawBar(tess, bar)

screen.exitonclick()