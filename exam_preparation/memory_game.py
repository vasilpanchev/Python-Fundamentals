sequence = input().split()
command = input()
moves = 0
while command != "end":
    index_1, index_2 = list(map(int, command.split()))
    moves += 1
    if index_1 == index_2 \
            or (index_1 not in range(len(sequence))
                or index_2 not in range(len(sequence))):
        middle = int(len(sequence) / 2)
        element = f"-{moves}a"
        for i in range(2):
            sequence.insert(middle, element)
        print(f"Invalid input! Adding additional elements to the board")
    else:
        if sequence[index_1] == sequence[index_2]:
            element = sequence.pop(index_1)
            if index_1 > index_2:
                sequence.pop(index_2)
            else:
                sequence.pop(index_2 - 1)
            print(f"Congrats! You have found matching elements - {element}!")
            if len(sequence) == 0:
                print(f"You have won in {moves} turns!")
                break
        else:
            print("Try again!")
    command = input()
else:
    print("Sorry you lose :(")
    print(' '.join(sequence))
