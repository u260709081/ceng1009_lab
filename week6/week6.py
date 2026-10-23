################## EXERCISE 1
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

################## EXERCISE 2
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

################## EXERCISE 3
import turtle

screen = turtle.Screen()
screen.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.color("blue")
tess.width(2)
tess.speed(0)

def drawSpiral(length, angle):
    length_inc = length
    cur_length = length
    for _ in range(80):
        tess.forward(cur_length)
        tess.right(angle)
        cur_length += length_inc

tess.penup()
tess.goto(-150, 0)
tess.pendown()
drawSpiral(2, 90)

tess.penup()
tess.goto(150, 0)
tess.pendown()
drawSpiral(2, 89)

screen.exitonclick()

################## EXERCISE 4
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

################## EXERCISE 5
import turtle

screen = turtle.Screen()
screen.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.color("pink")
tess.width(3)

tess.penup()
tess.backward(200)
tess.pendown()

star_length = 80

def draw_star():
    for _ in range(5):
        tess.forward(star_length)
        tess.right(144)

for _ in range(5):
    draw_star()
    tess.penup()
    tess.forward(350)
    tess.right(144)
    tess.pendown()

screen.exitonclick()

################## EXERCISE 6
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