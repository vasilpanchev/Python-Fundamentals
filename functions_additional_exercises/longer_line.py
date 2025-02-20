from math import sqrt


def closer_to_center(x1, y1, x2, y2):
    d1 = sqrt(x1 ** 2 + y1 ** 2)
    d2 = sqrt(x2 ** 2 + y2 ** 2)

    if d1 <= d2:
        x, y = x1, y1
        x_, y_ = x2, y2
    else:
        x, y = x2, y2
        x_, y_ = x1, y1

    return f"({int(x)}, {int(y)})({int(x_)}, {int(y_)})"


def line_length(x1, y1, x2, y2):
    x = abs(x1) + abs(x2)
    y = abs(y1) + abs(y2)

    line = sqrt(x ** 2 + y ** 2)

    return line


def longer_line(x1, y1, x2, y2, x3, y3, x4, y4):
    line1 = line_length(x1, y1, x2, y2)
    line2 = line_length(x3, y3, x4, y4)

    if line1 >= line2:
        return closer_to_center(x1, y1, x2, y2)
    else:
        return closer_to_center(x3, y3, x4, y4)


x1, y1, x2, y2, x3, y3, x4, y4 = float(input()), float(input()), float(input()), float(input()), float(input()), float(
    input()), float(input()), float(input())

print(longer_line(x1, y1, x2, y2, x3, y3, x4, y4))
