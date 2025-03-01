dragons = {}
order = []
number_of_dragons = int(input())
for i in range(number_of_dragons):
    dragon = input().split()

    dragon[2] = 45 if dragon[2] == "null" else int(dragon[2])
    dragon[3] = 250 if dragon[3] == "null" else int(dragon[3])
    dragon[4] = 10 if dragon[4] == "null" else int(dragon[4])

    dragon_type, dragon_name = dragon[0], dragon[1]
    dragon_stats = {"damage": dragon[2], "health": dragon[3], "armor": dragon[4]}

    if dragon_type not in dragons.keys():
        dragons[dragon_type] = {}
    dragons[dragon_type][dragon_name] = dragon_stats

for dragon_type in dragons.keys():
    total_damage = sum(dragon["damage"] for dragon in dragons[dragon_type].values())
    total_health = sum(dragon["health"] for dragon in dragons[dragon_type].values())
    total_armor = sum(dragon["armor"] for dragon in dragons[dragon_type].values())
    dragons_count = len(dragons[dragon_type])

    average_damage = total_damage / dragons_count
    average_health = total_health / dragons_count
    average_armor = total_armor / dragons_count

    print(f"{dragon_type}::({average_damage:.2f}/{average_health:.2f}/{average_armor:.2f})")

    for (dragon, stats) in sorted(dragons[dragon_type].items()):
        print(f'-{dragon} -> damage: {stats["damage"]}, health: {stats["health"]}, armor: {stats["armor"]}')
