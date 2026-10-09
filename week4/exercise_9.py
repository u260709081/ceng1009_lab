import turtle

leg_count = int(input("How many legs? "))

screen = turtle.Screen()
turt = turtle.Turtle()

angle = 360 / leg_count

for _ in range(leg_count):
    turt.forward(100)
    turt.backward(100)
    turt.right(angle)

screen.exitonclick()