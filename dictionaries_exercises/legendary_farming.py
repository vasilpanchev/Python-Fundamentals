key_materials = {"shards": 0, "fragments": 0, "motes": 0}
junk = {}
item_is_obtained = False
while not item_is_obtained:
    line = input()
    line_as_list = line.split()
    for i in range(0, len(line_as_list), 2):
        quantity = int(line_as_list[i])
        material = line_as_list[i + 1].lower()

        if material in key_materials:
            key_materials[material] += quantity
            if key_materials[material] >= 250:
                if material == "shards":
                    item = "Shadowmourne"
                elif material == "fragments":
                    item = "Valanyr"
                elif material.lower() == "motes":
                    item = "Dragonwrath"

                key_materials[material] -= 250
                item_is_obtained = True
                break
        else:
            if material not in junk:
                junk[material] = 0
            junk[material] += quantity

print(f"{item} obtained!")
for (material, quantity) in key_materials.items():
    print(f"{material}: {quantity}")
for (material, quantity) in junk.items():
    print(f"{material}: {quantity}")
