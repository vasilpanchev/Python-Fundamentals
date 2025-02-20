def smallest_number(a: int, b: int, c: int):
    if a <= b and a <= c:
        return a
    elif b <= a and b <= c:
        return b
    else:
        return c


num1 = int(input())
num2 = int(input())
num3 = int(input())

print(smallest_number(num1, num2, num3))
