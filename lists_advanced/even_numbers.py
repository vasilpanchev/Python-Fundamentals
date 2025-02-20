numbers = list(map(int, input().split(', ')))

indices_of_even_numbers = [i for i in range(len(numbers)) if numbers[i] % 2 == 0]

print(indices_of_even_numbers)
