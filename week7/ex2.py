import turtle

screen = turtle.Screen()
tess = turtle.Turtle()

def draw_star(turt: turtle.Turtle, n: int):
    for _ in range(n):
        turt.forward(100)
        turt.right(180 - 180 / n)

draw_star(tess, 9)
screen.exitonclick()