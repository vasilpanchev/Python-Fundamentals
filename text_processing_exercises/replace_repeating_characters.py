text = input()
result = ""
for i in range(len(text) - 1):
    character = text[i]
    if character != text[i + 1]:
        result += character

result += text[-1]
print(result)
