def exchange(nums: list, index):
    if index < 0 or index >= len(nums):
        print("Invalid index")
        return nums

    return nums[index + 1:] + nums[:index + 1]  # Proper rotation using slicing


def max_element(nums: list, num_type):
    filtered = [num for num in nums if (num % 2 == 0 if num_type == "even" else num % 2 != 0)]

    if not filtered:
        return "No matches"

    max_val = max(filtered)
    return max(i for i, num in enumerate(nums) if num == max_val)  # Get last occurrence


def min_element(nums: list, num_type):
    filtered = [num for num in nums if (num % 2 == 0 if num_type == "even" else num % 2 != 0)]

    if not filtered:
        return "No matches"

    min_val = min(filtered)
    return max(i for i, num in enumerate(nums) if num == min_val)  # Get last occurrence


def first(nums: list, count, num_type):
    if count < 0 or count > len(nums):  # Validate count
        return "Invalid count"

    filtered = [num for num in nums if (num % 2 == 0 if num_type == "even" else num % 2 != 0)]
    return filtered[:count]  # Get the first `count` elements


def last(nums: list, count, num_type):
    if count < 0 or count > len(nums):  # Validate count
        return "Invalid count"

    filtered = [num for num in nums if (num % 2 == 0 if num_type == "even" else num % 2 != 0)]
    return filtered[-count:] if count <= len(filtered) else filtered  # Extract correctly



def end(nums: list):
    return nums


def main():
    numbers = list(map(int, input().split()))
    command = input()
    while command != "end":
        command_parts = command.split()

        if command_parts[0] == "exchange":
            index = int(command_parts[1])
            numbers = exchange(numbers, index)

        elif command_parts[0] == "max":
            num_type = command_parts[1]
            print(max_element(numbers, num_type))

        elif command_parts[0] == "min":
            num_type = command_parts[1]
            print(min_element(numbers, num_type))

        elif command_parts[0] == "first":
            count = int(command_parts[1])
            num_type = command_parts[2]

            print(first(numbers, count, num_type))

        elif command_parts[0] == "last":
            count = int(command_parts[1])
            num_type = command_parts[2]

            print(last(numbers, count, num_type))

        command = input()

    else:
        print(end(numbers))


if __name__ == "__main__":
    main()
