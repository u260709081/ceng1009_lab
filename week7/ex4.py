def mySqrt(N: int):
    guess = N/2
    for _ in range(5):
        guess = (1/2) * (guess + N/guess)
    return guess

print(mySqrt(int(input("Enter N: "))))