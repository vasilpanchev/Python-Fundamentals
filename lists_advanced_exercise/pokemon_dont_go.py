distances = list(map(int, input().split()))
total_value = 0
while distances:
    current_index = int(input())

    if current_index < 0:
        pokemon_value = distances[0]
        distances[0] = distances[-1]

    elif current_index >= len(distances):
        pokemon_value = distances[-1]
        distances[-1] = distances[0]
    else:
        pokemon_value = distances.pop(current_index)

    total_value += pokemon_value
    for i in range(len(distances)):
        if distances[i] <= pokemon_value:
            distances[i] += pokemon_value
        else:
            distances[i] -= pokemon_value
else:
    print(total_value)
