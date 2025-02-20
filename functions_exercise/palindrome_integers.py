def is_palindrome(numbers: list):
    for number in numbers:
        reversed_number = ""
        current_number = number
        while current_number > 0:
            current_digit = current_number % 10
            reversed_number += str(current_digit)
            current_number = int(current_number / 10)

        if int(reversed_number) == number:
            print(True)
        else:
            print(False)


list_of_numbers = list(map(int, input().split(', ')))
is_palindrome(list_of_numbers)
