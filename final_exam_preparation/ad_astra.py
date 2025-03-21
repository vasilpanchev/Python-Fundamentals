import re


class AdAstra:
    pattern = r"([#|]{1})([A-Za-z\s]+)\1([0-3][0-9]/[0-1][0-9]/[0-9][0-9])\1(\d+)\1"

    def __init__(self, data: str):
        self.products = []
        self.total_calories = 0
        self.data = data
        self.days = 0

    def process_data(self):
        foods = re.finditer(self.pattern, self.data)
        for food in foods:
            self.products.append(f"Item: {food.group(2)}, Best before: {food.group(3)}, Nutrition: {food.group(4)}")
            self.total_calories += int(food.group(4))
        self.days = self.total_calories // 2000


def ad_astra_main():
    text = input()
    ad_astra_ = AdAstra(text)
    ad_astra_.process_data()
    print(f"You have food to last you for: {ad_astra_.days} days!")
    print('\n'.join(ad_astra_.products))

if __name__ == '__main__':
    ad_astra_main()