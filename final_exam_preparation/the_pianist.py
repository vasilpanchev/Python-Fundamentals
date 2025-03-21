class Pianist:
    def __init__(self):
        pass


def main():
    n = int(input())
    pieces = {}
    for _ in range(n):
        piece = input().split("|")
        piece_name, composer, key = piece[0], piece[1], piece[2]
        pieces[piece_name] = {"composer": composer, "key": key}

    command = input()
    while command != "Stop":
        command = command.split("|")
        action = command[0]
        if action == "Add":
            piece = command[1]
            composer = command[2]
            key = command[3]
            if piece in pieces.keys():
                print(f"{piece} is already in the collection!")
            else:
                pieces[piece] = {"composer": composer, "key": key}
                print(f"{piece} by {composer} in {key} added to the collection!")
        elif action == "Remove":
            piece = command[1]
            if piece in pieces.keys():
                del pieces[piece]
                print(f"Successfully removed {piece}!")
            else:
                print(f"Invalid operation! {piece} does not exist in the collection.")
        elif action == "ChangeKey":
            piece = command[1]
            new_key = command[2]
            if piece in pieces.keys():
                pieces[piece]["key"] = new_key
                print(f"Changed the key of {piece} to {new_key}!")
            else:
                print(f"Invalid operation! {piece} does not exist in the collection.")
        command = input()
    for (name, details) in pieces.items():
        composer = details["composer"]
        key = details["key"]
        print(f"{name} -> Composer: {composer}, Key: {key}")

if __name__ == '__main__':
    main()