import math


def closer_to_center(x1, y1, x2, y2):
    d1 = math.sqrt(x1 ** 2 + y1 ** 2)
    d2 = math.sqrt(x2 ** 2 + y2 ** 2)

    if d1 <= d2:
        x, y = x1, y1
    else:
        x, y = x2, y2

    return f"({int(x)}, {int(y)})"


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

print(closer_to_center(x1, y1, x2, y2))
