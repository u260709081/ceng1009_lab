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