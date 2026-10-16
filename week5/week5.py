# EXERCISE 1

import random

for _ in range(10):
    print(random.randint(0, 10))


###############################
# EXERCISE 2

import random

for _ in range(10):
    print(random.randint(25, 35))

###############################
# EXERCISE 3

import math

a = float(input("Enter a: "))
b = float(input("Enter b: "))
print(f"Hypothenuse of right triangle of sides {a} and {b} is {math.hypot(a, b)}")

###############################
# EXERCISE 4

import math

def areaOfCircle(r) :
    return math.pi * (r**2)

print(f"Area of circle of r=2 is {areaOfCircle(2)}")

###############################
# EXERCISE 5

import turtle

screen = turtle.Screen()
drawer = turtle.Turtle()

length = 100

for _ in range(5):
    drawer.forward(length)
    drawer.right(144)

screen.exitonclick()

###############################
# EXERCISE 6

import turtle

screen = turtle.Screen()
drawer = turtle.Turtle()

screen.bgcolor("lightgreen")
drawer.color("lightpink")

drawer.penup()
drawer.backward(60)
drawer.pensize(7)

for _ in range(5):
    drawer.pendown()
    for _ in range(4):
        drawer.forward(20)
        drawer.left(90)
    drawer.penup()
    drawer.forward(20+20)

screen.exitonclick()

###############################
# EXERCISE 7

import turtle

screen = turtle.Screen()
drawer = turtle.Turtle()

screen.bgcolor("lightgreen")
drawer.color("lightpink")
drawer.penup()

def draw_square(offset: int):
    drawer.backward(offset)
    drawer.pendown()

    drawer.left(90)
    drawer.forward(offset)
    for _ in range(3):
        drawer.right(90)
        drawer.forward(2 * offset)
    drawer.right(90)
    drawer.forward(offset)
    drawer.penup()

    drawer.right(90)
    drawer.forward(offset)


current_length = 20
for _ in range(5):
    draw_square(current_length / 2)
    current_length += 20

screen.exitonclick()