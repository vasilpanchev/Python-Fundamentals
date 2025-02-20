wagons = [0] * int(input())

while True:
    command = input().split()

    if command[0] == "End":
        print(wagons)
        break

    elif command[0] == "add":
        people_to_add = int(command[1])
        wagons[-1] += people_to_add

    elif command[0] == "insert":
        index = int(command[1])
        people = int(command[2])
        wagons[index] += people

    elif command[0] == "leave":
        index = int(command[1])
        people = int(command[2])
        wagons[index] -= people
