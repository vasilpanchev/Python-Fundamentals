numbers_as_strings = input().split()
to_remove = int(input())

numbers = []

for number in numbers_as_strings:
    numbers.append(int(number))

sorted_numbers = numbers.copy()
sorted_numbers.sort()

for i in range(to_remove):
    number_to_remove = sorted_numbers[i]
    numbers.remove(number_to_remove)

numbers_as_strings=[]

for number in numbers:
    numbers_as_strings.append(str(number))

print(', '.join(numbers_as_strings))

