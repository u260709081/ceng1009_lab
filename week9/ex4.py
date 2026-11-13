import math

def is_prime(N: int):
    if N < 2:
        return False
    # By trial division, LARGEST *small* factor is equal or less than sqrt(N)
    upper = int(math.sqrt(N))
    for factor in range(2, upper+1):
        if N % factor == 0:
            return False
    return True

print(is_prime(1))
print(is_prime(2))
print(is_prime(3))
print(is_prime(4))
print(is_prime(5))
print(is_prime(6))
print(is_prime(7))
print(is_prime(8))