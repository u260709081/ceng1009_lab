def digit_sum(n):
    sum = 0
    number = n
    while number > 0:
        sum += number % 10
        number //= 10
    return sum

print(digit_sum(1234))
print(digit_sum(0))