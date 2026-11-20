def sum_until_even(xs):
    total = 0
    for item in xs:
        if item % 2 == 0:
            return total
        total += item
    return total

print(sum_until_even([1,3,5,2,6]))