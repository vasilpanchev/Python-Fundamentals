class Pianist:

    def __init__(self):
        self.pieces = {}

    def initiate_pieces(self, n: int):
        for _ in range(n):
            piece = input().split("|")
            piece_name, composer, key = piece[0], piece[1], piece[2]
            self.pieces[piece_name] = {"composer": composer, "key": key}

    def add_piece(self, piece: str, composer: str, key: str):
        if piece in self.pieces.keys():
            return f"{piece} is already in the collection!"
        else:
            self.pieces[piece] = {"composer": composer, "key": key}
            return f"{piece} by {composer} in {key} added to the collection!"

    def remove_piece(self, piece: str):
        if piece in self.pieces.keys():
            del self.pieces[piece]
            return f"Successfully removed {piece}!"
        else:
            return f"Invalid operation! {piece} does not exist in the collection."

    def change_key(self, piece, new_key):
        if piece in self.pieces.keys():
            self.pieces[piece]["key"] = new_key
            return f"Changed the key of {piece} to {new_key}!"
        else:
            return f"Invalid operation! {piece} does not exist in the collection."

    def edit_pieces(self):
        command = input()
        while command != "Stop":
            command = command.split("|")
            action = command[0]
            if action == "Add":
                piece, composer, key = command[1], command[2], command[3]
                result = self.add_piece(piece, composer, key)
                print(result)
            elif action == "Remove":
                piece = command[1]
                result = self.remove_piece(piece)
                print(result)
            elif action == "ChangeKey":
                piece, new_key = command[1], command[2]
                result = self.change_key(piece, new_key)
                print(result)
            command = input()

    def __repr__(self):
        output = []
        for (name, details) in self.pieces.items():
            composer = details["composer"]
            key = details["key"]
            output.append(f"{name} -> Composer: {composer}, Key: {key}")
        return '\n'.join(output)


def main():
    pianist = Pianist()
    n = int(input())
    pianist.initiate_pieces(n)
    pianist.edit_pieces()
    print(pianist)


if __name__ == '__main__':
    main()
