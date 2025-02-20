def sum_numbers(a: int, b: int, c: int):
    return a + b


def subtract(a: int, b: int, c: int):
    return sum_numbers(a, b, c) - c


def add_and_subtract():
    a = int(input())
    b = int(input())
    c = int(input())

    return subtract(a, b, c)


print(add_and_subtract())
