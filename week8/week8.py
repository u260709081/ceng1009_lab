############ EXERCISE 1
def get_grade(mark: float):
    if   mark >= 90: return 'A'
    elif mark >= 80: return 'B'
    elif mark >= 70: return 'C'
    elif mark >= 60: return 'D'
    else:            return 'F'

for mark in [95,90,89.9,80,79.9,70,65,60,59.5,0]:
    print(get_grade(mark))

mark = float(input("Enter your mark: "))
print(f"Your mark of score {mark} is {get_grade(mark)}")

############ EXERCISE 2
import turtle

screen = turtle.Screen()
tess = turtle.Turtle()

screen.bgcolor("lightgreen")
tess.color("blue")
tess.width(2)

bars = [48, 117, 200, 240, 160, 260, 220]

BAR_WIDTH = 30

def chooseColor(height: int):
    if height >= 200: return 'red'
    elif height >= 100: return 'yellow'
    else: return 'green'

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

    t.color(chooseColor(height))
    t.end_fill()
    t.left(90)

for bar in bars:
    drawBar(tess, bar)

screen.exitonclick()

############ EXERCISE 3
import turtle

screen = turtle.Screen()
tess = turtle.Turtle()

screen.bgcolor("lightgreen")
tess.color("blue")
tess.width(2)

tess.speed(0)

bars = [48, 117, 200, 240, 160, 260, 220, -48, -210, -208, -145]

BAR_WIDTH = 30

def chooseColor(height: int):
    if height >= 200: return 'red'
    elif height >= 100: return 'yellow'
    else: return 'green'

def drawText(t: turtle.Turtle, height: int):
    t.left(90)
    if height < 0:
        draw_height = 0
    else:
        draw_height = height

    t.penup()
    t.forward(draw_height)
    t.left(90)
    t.forward(BAR_WIDTH)
    t.right(180)
    t.color("red")
    t.write(f"{height}")
    t.forward(BAR_WIDTH)
    t.right(90)
    t.forward(draw_height)
    t.left(90)
    t.pendown()

def drawBar(t: turtle.Turtle, height: int):
    t.left(90)

    t.color("blue")
    t.begin_fill()
    t.forward(height)
    t.right(90)

    t.color("blue")
    t.forward(BAR_WIDTH)
    t.right(90)
    t.forward(height)

    t.color(chooseColor(height))
    t.end_fill()
    t.left(90)

for bar in bars:
    drawBar(tess, bar)
    drawText(tess, bar)

screen.exitonclick()

############ EXERCISE 4
import math

def findHypot(a: float, b: float):
    return math.sqrt(a**2 + b**2)

print(f"Hypothenuse of triangle 3 4 is {findHypot(3, 4)}")