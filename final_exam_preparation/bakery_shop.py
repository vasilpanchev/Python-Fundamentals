foods = {}
all_sold_quantity = 0
command = input()
while command != "Complete":
    command = command.split()
    action, quantity, food = command[0], int(command[1]), command[2]
    if action == "Receive":
        if quantity > 0:
            if food not in foods:
                foods[food] = 0
            foods[food] += quantity
    elif action == "Sell":
        if food in foods:
            if foods[food] >= quantity:
                foods[food] -= quantity
                all_sold_quantity += quantity
                print(f"You sold {quantity} {food}.")
                if foods[food] == 0:
                    del foods[food]
            else:
                sold_quantity = foods[food]
                all_sold_quantity += sold_quantity
                foods[food] = 0
                del foods[food]
                print(f"There aren't enough {food}. You sold the last {sold_quantity} of them.")
        else:
            print(f"You do not have any {food}.")

    command = input()

for food, quantity in foods.items():
    print(f"{food}: {quantity}")
print(f"All sold: {all_sold_quantity} goods")
