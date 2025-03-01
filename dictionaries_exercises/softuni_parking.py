class Parking():
    def __init__(self):
        self.users = {}

    def register(self, username, license_plate_number):
        if username in self.users:
            return f"ERROR: already registered with plate number {self.users[username]}"
        self.users[username] = license_plate_number
        return f"{username} registered {license_plate_number} successfully"

    def unregister(self, username):
        if username not in self.users:
            return f"ERROR: user {username} not found"
        del self.users[username]
        return f"{username} unregistered successfully"

    def __repr__(self):
        return '\n'.join(
            f"{username} => {license_plate_number}" for (username, license_plate_number) in self.users.items())


def main():
    parking = Parking()
    commands = int(input())
    for _ in range(commands):
        command = input().split()
        action = command[0]
        if action == "register":
            username = command[1]
            license_plate_number = command[2]
            print(parking.register(username, license_plate_number))
        elif action == "unregister":
            username = command[1]
            print(parking.unregister(username))
    print(parking)


if __name__ == "__main__":
    main()
