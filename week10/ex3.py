def sum_evens(xs):
    total = 0
    for item in xs:
        if item % 2 == 0:
            total += item
    return total

print(sum_evens([1, 2, 3, 4, 5, 6]))