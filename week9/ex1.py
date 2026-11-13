def is_odd(n):
    return (n % 2) == 1

n = int(input(">"))
print(f"{n} is {['even', 'odd'][is_odd(n)]}")