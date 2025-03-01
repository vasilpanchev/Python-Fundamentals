text = input()
characters = {}
for character in text:
    if character != " ":
        if character not in characters:
            characters[character] = 0
        characters[character] += 1

for (character, times_in_string) in characters.items():
    print(f"{character} -> {times_in_string}")
