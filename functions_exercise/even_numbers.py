def is_even(a):
    return a % 2 == 0


list_of_numbers = list(map(int, input().split()))
filtered_list = list(filter(is_even, list_of_numbers))

print(filtered_list)
