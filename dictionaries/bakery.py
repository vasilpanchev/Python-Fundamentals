class Bakery:
    def __init__(self, food_and_quantities: str):
        self.food_and_quantities = food_and_quantities.split()
        self.products = {}

    def create_stock_table(self):
        for i in range(0, len(self.food_and_quantities), 2):
            key = self.food_and_quantities[i]
            value = int(self.food_and_quantities[i + 1])
            self.products[key] = value
        return self.products


food_and_quantities = input()
bakery = Bakery(food_and_quantities)
products_for_bakery = bakery.create_stock_table()
print(products_for_bakery)
