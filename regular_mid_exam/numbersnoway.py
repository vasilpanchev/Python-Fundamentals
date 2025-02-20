numbers = list(map(int, input().split()))
command = input()
while command != "Finish":
    action = command.split()
    if action[0] == "Add":
        value = int(action[1])
        numbers.append(value)
    elif action[0] == "Remove":
        value = int(action[1])
        if value in numbers:
            numbers.remove(value)
    elif action[0] == "Replace":
        value = int(action[1])
        replacement = int(action[2])
        if value in numbers:
            for i in range(len(numbers)):
                if numbers[i] == value:
                    numbers[i] = replacement
                    break
    elif action[0] == "Collapse":
        value = int(action[1])
        numbers = [number for number in numbers if number >= value]
    command = input()
print(*numbers, sep=' ')
