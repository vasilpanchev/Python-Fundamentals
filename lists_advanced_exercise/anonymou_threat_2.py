def merge(strings: list[str], start_index, end_index):
    # Ensure indices are within valid bounds
    start_index = max(0, start_index)
    end_index = min(len(strings) - 1, end_index)

    # Merge selected elements
    merged_string = ''.join(strings[start_index:end_index + 1])

    # Reconstruct the list
    strings = strings[:start_index] + [merged_string] + strings[end_index + 1:]
    return strings


def divide(strings: list[str], index, partitions):
    word = strings[index]
    part_size = len(word) // partitions
    remainder = len(word) % partitions

    divided_string = []
    start = 0

    for i in range(partitions):
        extra_char = 1 if i < remainder else 0  # Distribute remaining characters evenly
        divided_string.append(word[start:start + part_size + extra_char])
        start += part_size + extra_char

    # Reconstruct the list
    strings = strings[:index] + divided_string + strings[index + 1:]
    return strings


def main():
    list_of_strings = input().split()
    command = input()

    while command != "3:1":
        command = command.split()
        if command[0] == "merge":
            start_index = int(command[1])
            end_index = int(command[2])
            list_of_strings = merge(list_of_strings, start_index, end_index)
        elif command[0] == "divide":
            index = int(command[1])
            partitions = int(command[2])
            if partitions > 0:  # Ensure valid partitioning
                list_of_strings = divide(list_of_strings, index, partitions)

        command = input()

    print(' '.join(list_of_strings))


if __name__ == "__main__":
    main()
