locations = input()
command = input()
while command != "Travel":
    command = command.split()
    if command[0] == "Add":
        current_command = command[1].split(":")
        index = int(current_command[1])
        substring = current_command[2]
        if index in range(len(locations)):
            locations = locations[:index] + substring + locations[index:]
    elif command[0] == "Remove":
        current_command = command[1].split(":")
        start_index = int(current_command[1])
        end_index = int(current_command[2])
        if start_index in range(len(locations)) and end_index in range(len(locations)):
            locations = locations[:start_index] + locations[end_index + 1:]
    else:
        switch = command[0].split(":")
        old_string = switch[1]
        new_string = switch[2]
        if old_string in locations:
            locations = locations.replace(old_string, new_string)
    print(locations)
    command = input()
print(f"Ready for world tour! Planned stops: {locations}")
