text = input()

for i in range(len(text)):
    before = text[:i]
    after = text[i + 1:]
    current_character = chr(ord(text[i]) + 3)
    text = before + current_character + after

print(text)
