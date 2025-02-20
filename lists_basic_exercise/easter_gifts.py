gifts_string = input()
gifts = gifts_string.split()

command = input()

while command != "No Money":
    command_parts = command.split()

    if command_parts[0] == "OutOfStock":
        if command_parts[1] in gifts:
            for i in range(len(gifts)):
                if gifts[i] == command_parts[1]:
                    gifts[i] = "None"
    elif command_parts[0] == "Required":
        if 0 <= int(command_parts[2]) < len(gifts):
            gifts[int(command_parts[2])] = command_parts[1]
    elif command_parts[0] == "JustInCase":
        gifts[len(gifts) - 1] = command_parts[1]

    command = input()

for gift in gifts:
    if gift != "None":
        print(gift, end=' ')
