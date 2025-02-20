def factorial(number: int) -> int:
    if number <= 1:
        return 1
    return number * factorial(number - 1)


def factorial_division(a: int, b: int) -> float:
    a_fact = factorial(a)
    b_fact = factorial(b)
    fact_division = a_fact / b_fact
    return fact_division


num1 = int(input())
num2 = int(input())
print(f"{factorial_division(num1, num2):.2f}")
