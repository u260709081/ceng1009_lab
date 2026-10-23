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