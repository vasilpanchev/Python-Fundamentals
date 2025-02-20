money_as_string = input().split(", ")
money_as_integers = []

beggars = int(input())
start_index = 0
current_beggar_sum = 0

beggars_sums = []

for money in money_as_string:
    money_as_integers.append(int(money))

for current_beggar in range(beggars):
    for current_index in range(start_index, len(money_as_integers), beggars):
        current_beggar_sum += money_as_integers[current_index]
    start_index += 1
    beggars_sums.append(current_beggar_sum)
    current_beggar_sum = 0

print(beggars_sums)
