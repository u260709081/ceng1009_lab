def alternate_case(s):
    output = ""
    for i in range(len(s)):
        if i % 2 == 0:
            output += s[i].upper()
        else:
            output += s[i].lower()
    return output

print(alternate_case("hello world"))