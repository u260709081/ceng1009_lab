#################### EXERCISE 1
def sumTo(n: int):
    return n * (n+1) // 2

print(sumTo(int(input("Enter N: "))))

#################### EXERCISE 2
import turtle

screen = turtle.Screen()
tess = turtle.Turtle()

def draw_star(turt: turtle.Turtle, n: int, length: int):
    for _ in range(n):
        turt.forward(length)
        turt.right(180 - 180 / n)

draw_star(tess, 9, 100)
screen.exitonclick()

#################### EXERCISE 3
def sumTo(n: int):
    accumulated = 0
    for i in range(n+1):
        accumulated += i
    return accumulated

print(sumTo(int(input("Enter N: "))))

#################### EXERCISE 4
def mySqrt(N: int):
    guess = N/2
    for _ in range(5):
        guess = (1/2) * (guess + N/guess)
    return guess

print(mySqrt(int(input("Enter N: "))))

#################### EXERCISE 5
import turtle

screen = turtle.Screen()
tess = turtle.Turtle()
tess.shape("triangle")

def fancySquare(t: turtle.Turtle):
    for _ in range(4):
        t.stamp()
        t.forward(50)
        t.right(90)

fancySquare(tess)
screen.exitonclick()


#################### EXERCISE 6
def sign(N: int):
    if N > 0:
        return "positive"
    elif N == 0:
        return "zero"
    else:
        return "negative"

N = int(input("Enter N: "))
print(f"{N} is {sign(N)}")