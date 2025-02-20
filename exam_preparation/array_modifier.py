array = list(map(int, input().split()))
command = input()
while command != "end":
    action = command.split()
    if action[0] == "swap":
        index_1 = int(action[1])
        index_2 = int(action[2])
        array[index_1], array[index_2] = array[index_2], array[index_1]

    elif action[0] == "multiply":
        index_1 = int(action[1])
        index_2 = int(action[2])
        array[index_1] *= array[index_2]
    elif action[0] == "decrease":
        array = [number - 1 for number in array]
    command = input()

print(*array, sep=', ')
