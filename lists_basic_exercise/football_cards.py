#a = [f"A-{x}" for x in range(1, 12)]
#b = [f"B-{x}" for x in range(1, 12)]


a = [str(x) for x in range(1, 12)]
b = [str(x) for x in range(1, 12)]

is_terminated = False

str_command = input()
command_list = str_command.split(' ')

for command in command_list:
    team, player = command.split("-")
    if team == 'A' and player in a:
        a.remove(player)
    elif team == 'B' and player in b:
        b.remove(player)

    if len(a) < 7 or len(b) < 7:
        is_terminated = True
        break


print(f"Team A - {len(a)}; Team B - {len(b)}")

if is_terminated:
    print("Game was terminated")
