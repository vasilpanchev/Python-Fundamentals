sequence = input()

digits = ""
letters = ""
other = ""

for char in sequence:
    if char.isdigit():
        digits += char
    elif char.isalpha():
        letters += char
    else:
        other += char

print(digits)
print(letters)
print(other)
