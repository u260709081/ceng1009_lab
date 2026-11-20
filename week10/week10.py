################### EX1
L = [76, 92.3, "hello", True, 4, 76]

L.append("apple")
L.append(76)
L.insert(3, "cat")
L.insert(0, "hello")

C = L.count(76)
L.remove(76)
L.pop(L.index(True))

################### EX2
def sum_of_squares(xs):
    total = 0
    for item in xs:
        total += item**2
    return total

print(sum_of_squares([2, 3, 4]))

################### EX3
def sum_evens(xs):
    total = 0
    for item in xs:
        if item % 2 == 0:
            total += item
    return total

print(sum_evens([1, 2, 3, 4, 5, 6]))

################### EX4
def count_fives(xs):
    count = 0
    for item in xs:
        if len(item) == 5:
            count += 1
    return count

print(count_fives(["hello", "google", "aeb", "health"]))

################### EX5
def sum_until_even(xs):
    total = 0
    for item in xs:
        if item % 2 == 0:
            return total
        total += item
    return total

print(sum_until_even([1,3,5,2,6]))

################### EX6
def count_until_sam(xs):
    count = 0
    for item in xs:
        if item == "sam":
            return count + 1
        count += 1
    return count

print(count_until_sam(["ae", "john", "johannes", "anna", "sam", "george"]))

################### EX7
def replace(s, old, new):
    return new.join(s.split(old))

print(replace("Mississippi", "i", "I"))

################### EX8
def max(ints):
    max = ints[0]
    for item in ints:
        if item > max:
            max = item
    return max

print(max([0,1,5,-1, 10]))
