############ EXERCISE 1
def fizz_buzz(n):
    for i in range(1, n+1):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 5 == 0:
            print("Buzz")
        elif i % 3 == 0:
            print("Fizz")
        else:
            print(i)

fizz_buzz(16)

############ EXERCISE 2
def digit_sum(n):
    sum = 0
    number = n
    while number > 0:
        sum += number % 10
        number //= 10
    return sum

print(digit_sum(1234))
print(digit_sum(0))

############ EXERCISE 3
def alternate_case(s):
    output = ""
    for i in range(len(s)):
        if i % 2 == 0:
            output += s[i].upper()
        else:
            output += s[i].lower()
    return output

print(alternate_case("hello world"))

############ EXERCISE 4
import turtle

scr = turtle.Screen()
tes = turtle.Turtle()

scr.bgcolor("lightgreen")
tes.pensize(3)
tes.penup()
tes.back(2 * 60)
tes.pendown()

def draw_polygon(t, sides, length):
    turn_angle = 360 / sides

    for _ in range(sides):
        t.forward(length)
        t.left(turn_angle)

for sides, color in [(3, "red"), (4, "yellow"), (5, "blue")]:
    tes.color(color)
    draw_polygon(tes, sides, 60)
    tes.penup()
    tes.forward(60+60)
    tes.pendown()


scr.exitonclick()

############ EXERCISE 5
import turtle

scr = turtle.Screen()
tes = turtle.Turtle()

scr.bgcolor("lightgreen")
def filled_square(t, side, color):
    t.color(color)
    t.begin_fill()
    for _ in range(4):
        t.forward(side)
        t.left(90)
    t.end_fill()

for index in range(5):
    if index % 2 == 0:
        filled_square(tes, 50, "red")
    else:
        filled_square(tes, 50, "blue")
    tes.penup()
    tes.forward(50 + 20)
    tes.pendown()

scr.exitonclick()

############ EXERCISE 6
import turtle

scr = turtle.Screen()
tes = turtle.Turtle()

def draw_square(t, size):
    for _ in range(4):
        t.forward(size)
        t.left(90)

scr.bgcolor("lightgreen")
tes.pensize(2)

for _ in range(12):
    draw_square(tes, 80)
    tes.left(360 / 12)

scr.exitonclick()

############ EXERCISE 7
import turtle

scr = turtle.Screen()
scr.bgcolor("lightgreen")

tes = turtle.Turtle()
tes.penup()
tes.goto((-120, +120))
tes.speed(0)

def square(t, size):
    t.pendown()
    for _ in range(4):
        t.forward(size)
        t.right(90)
    t.penup()

def filled_square(t, size):
    t.begin_fill()
    square(t, size)
    t.end_fill()

square(tes, 240)

for row in range(6):
    for col in range(6):
        if (row+col) % 2 == 0: continue
        goto_x = -120 + 40 * col
        goto_y = 120 - 40 * row
        tes.goto((goto_x, goto_y))
        filled_square(tes, 40)

scr.exitonclick()