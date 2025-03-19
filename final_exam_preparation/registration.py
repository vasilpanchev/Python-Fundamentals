username = input()
command = input()
while command != "Registration":
    command = command.split()
    action = command[0]

    if action == "Letters":
        mode = command[1]
        new_username = ""
        if mode == "Lower":
            for letter in username:
                new_username += letter.lower()
        elif mode == "Upper":
            for letter in username:
                new_username += letter.upper()
        username = new_username
        print(username)
    elif action == "Reverse":
        start_index = int(command[1])
        end_index = int(command[2])
        if start_index in range(len(username)) and end_index in range(len(username)):
            substring = username[start_index:end_index + 1]
            print(substring[::-1])
    elif action == "Substring":
        substring = command[1]
        if substring in username:
            username = username.replace(substring, "")
            print(username)
        else:
            print(f"The username {username} doesn't contain {substring}")
    elif action == "Replace":
        char = command[1]
        username = username.replace(char, "-")
        print(username)
    elif action == "IsValid":
        char = command[1]
        if char in username:
            print("Valid username.")
        else:
            print(f"{char} must be contained in your username.")

    command = input()
