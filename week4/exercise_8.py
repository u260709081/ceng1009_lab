import turtle
import math

screen = turtle.Screen()
turt = turtle.Turtle("turtle")
turt.color("#0000FF")

turt.stamp()

for angle in range(0, 360, 30):
    x = 100 * math.cos(angle * math.pi/180)
    y = 100 * math.sin(angle * math.pi/180)

    turt.penup()
    turt.goto((x, y))
    turt.pendown()
    
    turt.setheading(angle)
    turt.backward(8)
    turt.forward(8)

    turt.penup()
    turt.forward(13)
    turt.pendown()
    
    turt.stamp()

turt.penup()
turt.home()
turt.pendown()

screen.exitonclick()