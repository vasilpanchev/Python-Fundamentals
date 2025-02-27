class Stock:
    def __init__(self, products_and_quantities: str):
        self.products_and_quantities = products_and_quantities.split()
        self.products_and_quantities = self.products_to_dictionary(self.products_and_quantities)

    def check_for_product(self, product_to_check: str):
        if product_to_check in self.products_and_quantities:
            quantity = self.products_and_quantities[product_to_check]
            return f"We have {quantity} of {product_to_check} left"
        else:
            return f"Sorry, we don't have {product_to_check}"

    def products_to_dictionary(self, products: list):
        products_dictionary = {}
        for i in range(0, len(products), 2):
            key = products[i]
            value = int(products[i + 1])
            products_dictionary[key] = value
        return products_dictionary


def main():
    products = input()
    products_to_check = input().split()

    stock = Stock(products)
    for product_to_check in products_to_check:
        print(stock.check_for_product(product_to_check))


if __name__ == "__main__":
    main()
