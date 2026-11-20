def sum_of_squares(xs):
    total = 0
    for item in xs:
        total += item**2
    return total

print(sum_of_squares([2, 3, 4]))