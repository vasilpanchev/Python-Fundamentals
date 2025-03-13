def equal_dashes(text: str) -> bool:
    letter_count = 0
    dash_count = string1.count('-')
    for char in string1:
        if char.isalpha():
            letter_count += 1
    if dash_count % (letter_count - 1) != 0:
        return False
    return True


string1 = "B--A-N-A-N"
vowels = ["A, E, I, O, U"]

print(equal_dashes(string1))

string1 = string1.replace("-", '')
print(string1)

consonant_letters = 0
vowel_letters = 0
is_authentic = True
if string1[0] not in vowels and string1[-1] not in vowels:
    for letter in string1:
        if letter.upper() in vowels:
            vowel_letters += 1
            if consonant_letters != vowel_letters - 1:
                is_authentic = False
                break
        else:
            consonant_letters += 1
    if is_authentic:
        print("YES")
        exit()
