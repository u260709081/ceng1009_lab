import turtle

screen = turtle.Screen()
turt = turtle.Turtle()
CORNER_LENGTH = 80

def draw_regular_polygon(coord: tuple[int, int], sides: int):
    outer_angle = 360 / sides

    turt.penup()
    turt.goto(coord)
    turt.pendown()

    for _ in range(sides):
        turt.forward(CORNER_LENGTH)
        turt.left(outer_angle)

y_offset = 100
x_offset = 250
draw_regular_polygon((-x_offset,+y_offset,), 3)
draw_regular_polygon((-x_offset,-y_offset,), 4)
draw_regular_polygon((+x_offset,+y_offset,), 6)
draw_regular_polygon((+x_offset,-y_offset,), 8)

screen.exitonclick()