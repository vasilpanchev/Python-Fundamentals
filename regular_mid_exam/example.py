names = []
while True:
    command = input()
    if command == 'End':
        break
    name = command
    names.append(name)
print(', '.join(names))
