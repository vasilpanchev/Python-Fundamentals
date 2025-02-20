def positive_numbers(numbers: list[int]) -> str:
    return ', '.join([str(number) for number in numbers if number >= 0])


def negative_numbers(numbers: list[int]) -> str:
    return ', '.join([str(number) for number in numbers if number < 0])


def even_numbers(numbers: list[int]) -> str:
    return ', '.join([str(number) for number in numbers if number % 2 == 0])


def odd_numbers(numbers: list[int]) -> str:
    return ', '.join([str(number) for number in numbers if number % 2 == 1])


numbers = input().split(', ')
numbers = [int(number) for number in numbers]

print(f"Positive: {positive_numbers(numbers)}")
print(f"Negative: {negative_numbers(numbers)}")
print(f"Even: {even_numbers(numbers)}")
print(f"Odd: {odd_numbers(numbers)}")
