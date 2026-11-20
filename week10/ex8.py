def max(ints):
    max = ints[0]
    for item in ints:
        if item > max:
            max = item
    return max

print(max([0,1,5,-1, 10]))