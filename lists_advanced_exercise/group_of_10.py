from math import ceil

sequence = list(map(int, input().split(', ')))

number_of_groups = ceil((max(sequence) / 10))

groups = [[] for _ in range(number_of_groups)]

for i in range(len(sequence)):
    number = sequence[i]
    group = int((number - 1) / 10)
    groups[group].append(number)

for i in range(len(groups)):
    print(f"Group of {i + 1}0's: {groups[i]}")
