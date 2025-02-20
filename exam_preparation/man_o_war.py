pirate_ship = list(map(int, input().split('>')))
warship = list(map(int, input().split('>')))
maximum_health_capacity = int(input())
stalemate = False
command = input()
while command != "Retire":
    action = command.split()
    if action[0] == "Fire":
        index = int(action[1])
        if index in range(len(warship)):
            damage = int(action[2])
            warship[index] -= damage
            if warship[index] <= 0:
                print(f"You won! The enemy ship has sunken.")
                exit()

    elif action[0] == "Defend":
        start_index = int(action[1])
        end_index = int(action[2])
        if (start_index in range(len(pirate_ship))
                and end_index in range(len(pirate_ship))):
            damage = int(action[3])
            for i in range(start_index, end_index + 1):
                pirate_ship[i] -= damage
                if pirate_ship[i] <= 0:
                    print(f"You lost! The pirate ship has sunken.")
                    exit()

    elif action[0] == "Repair":
        index = int(action[1])
        if index in range(len(pirate_ship)):
            health = int(action[2])
            pirate_ship[index] += health
            if pirate_ship[index] > maximum_health_capacity:
                pirate_ship[index] = maximum_health_capacity

    elif action[0] == "Status":
        count = 0
        for i in range(len(pirate_ship)):
            section_health_percentage = pirate_ship[i] / maximum_health_capacity * 100
            if section_health_percentage < 20:
                count += 1
        print(f"{count} sections need repair.")

    command = input()
else:
    pirate_ship_sum = sum(pirate_ship)
    warship_sum = sum(warship)
    print(f"Pirate ship status: {pirate_ship_sum}")
    print(f"Warship status: {warship_sum}")
