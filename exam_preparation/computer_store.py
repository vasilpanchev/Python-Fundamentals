parts_prices = [0]
command = input()
while command != "regular" and command != "special":
    price = float(command)
    if price < 0:
        print("Invalid price!")
    else:
        parts_prices.append(price)
    command = input()

customer_type = command
total_price = sum(parts_prices)
if total_price == 0:
    print("Invalid order!")
else:
    taxes = 0.20 * total_price
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total_price:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    total_price += taxes
    if customer_type == "special":
        total_price -= 0.10 * total_price
    print(f"Total price: {total_price:.2f}$")
