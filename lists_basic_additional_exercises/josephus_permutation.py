numbers = input().split()
k = int(input())

execution_circle = []

i = 0
while numbers:
    i += k - 1
    while i >= len(numbers):
        i -= len(numbers)

    execution_circle.append(numbers[i])
    numbers.pop(i)

print(f"[{','.join(execution_circle)}]")
