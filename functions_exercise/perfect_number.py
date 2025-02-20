def aliquot_sum(number: int):
    dividers = []
    for divider in range(1, number):
        if number % divider == 0:
            dividers.append(divider)
    if sum(dividers) == number:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


num = int(input())
print(aliquot_sum(num))
