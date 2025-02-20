def validate_password(password: str):
    password_length = len(password)
    digits_count = 0
    is_alnum = password.isalnum()
    is_valid = True

    for i in range(password_length):
        if password[i].isdigit():
            digits_count += 1

    if not 6 <= password_length <= 10:
        is_valid = False
        print("Password must be between 6 and 10 characters")
    if not is_alnum:
        is_valid = False
        print("Password must consist only of letters and digits")
    if digits_count < 2:
        is_valid = False
        print("Password must have at least 2 digits")

    if is_valid:
        print("Password is valid")


user_password = input()
validate_password(user_password)
