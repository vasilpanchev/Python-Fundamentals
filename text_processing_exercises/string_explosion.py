line = input()
result = ""
strength = 0
for i in range(len(line) - 1):
    if line[i] == ">":
        strength += int(line[i + 1])
    elif strength > 0:
        strength -= 1
        continue
    result += line[i]

result += line[-1]
print(result)
