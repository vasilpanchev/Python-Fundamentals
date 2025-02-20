def characters_in_range(a, b):
    result = ''
    for i in range(ord(a) + 1, ord(b)):
        result += (chr(i) + " ")

    return result


char1 = input()
char2 = input()

print(characters_in_range(char1, char2))
