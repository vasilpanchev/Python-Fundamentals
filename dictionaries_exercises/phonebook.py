phone_numbers = {}
contacts = input()

while '-' in contacts:
    name, phone_number = contacts.split('-')
    phone_numbers[name] = phone_number
    contacts = input()

contacts = int(contacts)

for _ in range(contacts):
    name = input()
    if name in phone_numbers:
        print(f"{name} -> {phone_numbers[name]}")
    else:
        print(f"Contact {name} does not exist.")
