sequence_as_strings = input().split()
index_sequence = []
message = []

string = list(input())

for number in sequence_as_strings:
    current_number = int(number)
    current_sum = 0
    while current_number > 0:
        current_sum += current_number % 10
        current_number //= 10
    index_sequence.append(current_sum)

for index in index_sequence:
    while index >= len(string):
        index -= len(string)

    message.append(string[index])
    string.pop(index)

print(''.join(message))
