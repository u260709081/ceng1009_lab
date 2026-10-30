def sign(N: int):
    if N > 0:
        return "positive"
    elif N == 0:
        return "zero"
    else:
        return "negative"

N = int(input("Enter N: "))
print(f"{N} is {sign(N)}")