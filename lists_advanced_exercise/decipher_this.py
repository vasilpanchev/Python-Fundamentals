words = input().split()
deciphered_words = []
for i in range(len(words)):
    word = list(words[i])
    char_code = []
    if word[0].isdigit() and word[1].isdigit() and word[2].isdigit():
        char_code_int = int(''.join(word[:3]))
        word = word[3:]
    else:
        char_code_int = int(''.join(word[:2]))
        word = word[2:]

    word[0], word[-1] = word[-1], word[0]
    letter = chr(char_code_int)
    word_as_string = f"{letter}{''.join(word)}"
    deciphered_words.append(word_as_string)

print(' '.join(deciphered_words))
