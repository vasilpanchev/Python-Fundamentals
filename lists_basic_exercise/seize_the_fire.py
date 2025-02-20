fires_string = input()
fires = fires_string.split("#")

water = int(input())

effort = 0
completed_cells = []

for i in range(len(fires)):
    fire_type, cell = fires[i].split(" = ")
    if fire_type == "Low" and 1 <= int(cell) <= 50 and (water - int(cell)) >= 0:
        completed_cells.append(int(cell))
        water -= int(cell)
        effort += int(cell) * 0.25
    elif fire_type == "Medium" and 51 <= int(cell) <= 80 and (water - int(cell)) >= 0:
        completed_cells.append(int(cell))
        water -= int(cell)
        effort += int(cell) * 0.25
    elif fire_type == "High" and 81 <= int(cell) <= 125 and (water - int(cell)) >= 0:
        completed_cells.append(int(cell))
        water -= int(cell)
        effort += int(cell) * 0.25

    if water == 0:
        break

print("Cells:")
for cell in completed_cells:
    print(f" - {cell}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {sum(completed_cells)}")
