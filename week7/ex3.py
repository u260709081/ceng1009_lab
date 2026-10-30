def sumTo(n: int):
    accumulated = 0
    for i in range(n+1):
        accumulated += i
    return accumulated

print(sumTo(int(input("Enter N: "))))