def calculate(operator: str, a: int, b: int):
    if operator == "multiply":
        return a * b
    if operator == "divide":
        return int(a / b)
    if operator == "add":
        return a + b
    if operator == "subtract":
        return a - b


operator = input()
a = int(input())
b = int(input())

print(calculate(operator, a, b))
