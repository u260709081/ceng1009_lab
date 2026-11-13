def remove_all(main: str, substr: str):
    return main.replace(substr, "")

print(remove_all(input("1> "), input("2> ")))