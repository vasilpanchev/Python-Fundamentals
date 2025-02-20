def order(item: str, quantity: int):
    if item == "coffee":
        return quantity * 1.5
    elif item == "coke":
        return quantity * 1.4
    elif item == "water":
        return quantity * 1
    elif item == "snacks":
        return quantity * 2


item_to_order = input()
quantity_to_order = int(input())
print(f"{order(item_to_order, quantity_to_order):.2f}")
