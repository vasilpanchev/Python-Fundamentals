from math import floor

TICKET_PRICE = 150
MARKUP = 1.40

items_string = input()
items = items_string.split("|")

budget = float(input())

old_prices = []
new_prices = []

for i in range(len(items)):
    item_type, price = items[i].split('->')
    if item_type == "Clothes" and float(price) <= 50 and (budget - float(price)) >= 0:
        old_prices.append(float(price))
        budget -= float(price)
        new_prices.append(float(price) * MARKUP)
    elif item_type == "Shoes" and float(price) <= 35 and (budget - float(price)) >= 0:
        old_prices.append(float(price))
        budget -= float(price)
        new_prices.append(float(price) * MARKUP)
    elif item_type == "Accessories" and float(price) <= 20.50 and (budget - float(price)) >= 0:
        old_prices.append(float(price))
        budget -= float(price)
        new_prices.append(float(price) * MARKUP)

    if budget == 0:
        break

profit = sum(new_prices) - sum(old_prices)
total_money = sum(new_prices) + budget

new_prices_as_strings = []
for new_price in new_prices:
    new_prices_as_strings.append(f"{new_price:.2f}")

print(' '.join(new_prices_as_strings))
print(f"Profit: {profit:.2f}")

if total_money >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")
