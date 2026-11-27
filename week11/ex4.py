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