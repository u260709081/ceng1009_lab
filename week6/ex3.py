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