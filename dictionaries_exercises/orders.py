products = {}
command = input()
while command != "buy":
    product_data = command.split()
    name, price, quantity = product_data[0], float(product_data[1]), int(product_data[2])
    if name not in products:
        products[name] = {"price": 0.0, "quantity": 0}
    products[name]["price"] = price
    products[name]["quantity"] += quantity
    command = input()

for (name, product_data) in products.items():
    total_price = product_data["price"] * product_data["quantity"]
    print(f"{name} -> {total_price:.2f}")
