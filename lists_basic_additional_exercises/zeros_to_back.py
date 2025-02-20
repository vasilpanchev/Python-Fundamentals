numbers_as_strings = input().split(", ")
numbers = []

length = len(numbers_as_strings)

while "0" in numbers_as_strings:
    numbers_as_strings.remove("0")

zeros = length - len(numbers_as_strings)
for _ in range(zeros):
    numbers_as_strings.append("0")

for num in numbers_as_strings:
    numbers.append(int(num))

print(numbers)
