def remove_dups(main: str):
    result = ""
    for character in main:
        if character in result: continue
        result += character
    return result

print(remove_dups("Hello world!"))