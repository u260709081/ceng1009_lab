def count_fives(xs):
    count = 0
    for item in xs:
        if len(item) == 5:
            count += 1
    return count

print(count_fives(["hello", "google", "aeb", "health"]))