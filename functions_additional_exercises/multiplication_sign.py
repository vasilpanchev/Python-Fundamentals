def multiplication_sign(x, y, z):
    negative_count = 0
    if x == 0 or y == 0 or z == 0:
        return "zero"

    if x < 0:
        negative_count += 1
    if y < 0:
        negative_count += 1
    if z < 0:
        negative_count += 1

    if negative_count % 2 == 0:
        return "positive"
    else:
        return "negative"


num1 = int(input())
num2 = int(input())
num3 = int(input())

print(multiplication_sign(num1, num2, num3))
