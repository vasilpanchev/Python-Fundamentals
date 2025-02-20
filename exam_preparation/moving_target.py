targets = list(map(int, input().split()))
command = input()
while command != "End":
    command = command.split()
    action = command[0]
    if action == "Shoot":
        index = int(command[1])
        power = int(command[2])
        if index in range(len(targets)):
            targets[index] -= power
            if targets[index] <= 0:
                targets.pop(index)
    elif action == "Add":
        index = int(command[1])
        value = int(command[2])
        if index in range(len(targets)):
            targets.insert(index, value)
        else:
            print("Invalid placement!")
    elif action == "Strike":
        index = int(command[1])
        radius = int(command[2])
        start = index - radius
        end = index + radius
        if start >= 0 and end < len(targets):
            targets = targets[:start] + targets[end + 1:]
        else:
            print("Strike missed!")

    command = input()

print(*targets, sep="|")
