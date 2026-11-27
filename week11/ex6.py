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