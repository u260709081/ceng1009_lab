def print_trangular_numbers(n: int):
    for i in range(1, n+1):
        print(i, " ", i * (i+1) // 2)

print_trangular_numbers(5)