class ImitationGame:
    def __init__(self, encrypted_message: str):
        self.encrypted_message = encrypted_message

    def move(self, number_of_letters: int):
        to_back = self.encrypted_message[:number_of_letters]
        self.encrypted_message = self.encrypted_message[number_of_letters:] + to_back

    def insert(self, index: int, value: str):
        self.encrypted_message = self.encrypted_message[:index] + value + self.encrypted_message[index:]

    def change_all(self, substring: str, replacement: str):
        if substring in self.encrypted_message:
            self.encrypted_message = self.encrypted_message.replace(substring, replacement)

    def play(self, commands: list[str]):
        for command in commands:
            command = command.split('|')
            action = command[0]
            if action == "Move":
                number_of_letters = int(command[1])
                self.move(number_of_letters)
            elif action == "Insert":
                index = int(command[1])
                value = command[2]
                self.insert(index, value)
            elif action == "ChangeAll":
                substring = command[1]
                replacement = command[2]
                self.change_all(substring, replacement)

        return self.encrypted_message


def imitation_game_main():
    message = input()
    imitation_game = ImitationGame(message)
    commands = gather_commands()
    result = imitation_game.play(commands)
    print(f"The decrypted message is: {result}")


def gather_commands():
    commands = []
    command = input()
    while command != "Decode":
        commands.append(command)
        command = input()
    return commands


if __name__ == "__main__":
    imitation_game_main()
