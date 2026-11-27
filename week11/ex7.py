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