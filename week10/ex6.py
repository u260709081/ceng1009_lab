def count_until_sam(xs):
    count = 0
    for item in xs:
        if item == "sam":
            return count + 1
        count += 1
    return count

print(count_until_sam(["ae", "john", "johannes", "anna", "sam", "george"]))