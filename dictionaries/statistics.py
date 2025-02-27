class Statistics:
    def __init__(self):
        self.products = {}

    def add_product(self, key: str, quantity: int):
        if key not in self.products:
            self.products[key] = 0
        self.products[key] += quantity

    def __repr__(self):
        result = "Products in stock:\n"
        for (product, quantity) in self.products.items():
            result += f"- {product}: {quantity}\n"
        result += f"Total Products: {len(self.products.keys())}\n"
        result += f"Total Quantity: {sum(self.products.values())}"
        return result


def main():
    statistic = Statistics()
    command = input()
    while command != "statistics":
        key, value = command.split(': ')
        quantity = int(value)
        statistic.add_product(key, quantity)
        command = input()
    print(statistic)


if __name__ == "__main__":
    main()
