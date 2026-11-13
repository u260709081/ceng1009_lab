######### EXERCISE 1
def is_odd(n):
    return (n % 2) == 1

n = int(input(">"))
print(f"{n} is {['even', 'odd'][is_odd(n)]}")

######### EXERCISE 2
def is_leap_year(year: int):
    if year % 400 == 0: return True
    if year % 100 == 0: return False
    if year % 4 == 0: return True
    return False


print(is_leap_year(2026))
print(is_leap_year(2027))
print(is_leap_year(2028))
print(is_leap_year(2029))

######### EXERCISE 3
def print_trangular_numbers(n: int):
    for i in range(1, n+1):
        print(i, " ", i * (i+1) // 2)

print_trangular_numbers(5)

######### EXERCISE 4
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

######### EXERCISE 5
def reverse_string(string: str): 
    result = ""
    for character in string[::-1]:
        result += character
    return result

print(reverse_string(input("> ")))

######### EXERCISE 6
def remove_all(main: str, substr: str):
    return main.replace(substr, "")

print(remove_all(input("1> "), input("2> ")))

######### EXERCISE 7
def substitute(to_cipher: str, map: str):
    result = ""
    for character in to_cipher:
        index = ord(character.lower()) - ord('a')
        if (index >= len(map)) or (index < 0):
            result += character
            continue
        resultant = map[index]
        if ord(character) < ord('a'):
            resultant = resultant.upper()
        result += resultant
    return result

print(substitute("the quick brown fox jumps over thirteen lazy dogs", 'zyxwvutsrqponmlkjihgfedcba'))

######### EXERCISE 8
def remove_dups(main: str):
    result = ""
    for character in main:
        if character in result: continue
        result += character
    return result

print(remove_dups("Hello world!"))