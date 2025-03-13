strings = input().split()
if len(strings[0]) < len(strings[1]):
    leftover = strings[1][len(strings[0]):]
else:
    leftover = strings[0][len(strings[1]):]

shorter_word = min(len(word) for word in strings)
total_sum = 0
for i in range(shorter_word):
    char1 = ord(strings[0][i])
    char2 = ord(strings[1][i])
    total_sum += char1 * char2

for char in leftover:
    char_value = ord(char)
    total_sum += char_value

print(total_sum)
