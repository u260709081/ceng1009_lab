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