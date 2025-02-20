def round_list(numbers: list) -> list:
    rounded_list = []
    for number in numbers:
        rounded_list.append(round(number))

    return rounded_list


numbers_to_round = list(map(float, input().split(' ')))
print(round_list(numbers_to_round))
