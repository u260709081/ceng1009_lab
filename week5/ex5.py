import turtle

screen = turtle.Screen()
drawer = turtle.Turtle()

def draw_star(t, length: int):
    for _ in range(5):
        t.forward(length)
        t.right(144)

draw_star(drawer, 100)
screen.exitonclick()