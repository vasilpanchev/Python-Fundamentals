command = input()

while command != "end":
    word = command
    reversed_word = ""
    for letter in reversed(word):
        reversed_word += letter
    print(f"{word} = {reversed_word}")
    command = input()
