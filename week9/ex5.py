def reverse_string(string: str): 
    result = ""
    for character in string[::-1]:
        result += character
    return result

print(reverse_string(input("> ")))