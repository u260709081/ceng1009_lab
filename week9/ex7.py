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