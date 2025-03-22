class Plants:
    def __init__(self):
        self.plants = {}

    def initiate_plants(self, n: int):
        for _ in range(n):
            line = input()
            plant, rarity = line.split("<->")
            self.plants[plant] = {"rarity": rarity, "ratings": []}

    def rate(self, plant: str, rating: int):
        if plant not in self.plants.keys():
            return "error"
        self.plants[plant]["ratings"].append(rating)

    def update(self, plant: str, new_rarity: str):
        if plant not in self.plants.keys():
            return "error"
        self.plants[plant]["rarity"] = new_rarity

    def reset(self, plant):
        if plant not in self.plants.keys():
            return "error"
        self.plants[plant]["ratings"] = []

    @staticmethod
    def check_for_error(result):
        if result == "error":
            print("error")

    def exhibit(self):
        print("Plants for the exhibition:")
        for plant, details in self.plants.items():
            rarity = details["rarity"]
            if len(details["ratings"]) == 0:
                average_rating = 0
            else:
                average_rating = sum(details["ratings"]) / len(details["ratings"])
            print(f"- {plant}; Rarity: {rarity}; Rating: {average_rating:.2f}")

    def process_plants(self):
        command = input()
        while command != "Exhibition":
            action, details = command.split(": ")
            if action == "Rate":
                plant, rating = details.split(" - ")
                rating = int(rating)
                result = self.rate(plant, rating)
                self.check_for_error(result)
            elif action == "Update":
                plant, new_rarity = details.split(" - ")
                result = self.update(plant, new_rarity)
                self.check_for_error(result)
            elif action == "Reset":
                plant = details
                result = self.reset(plant)
                self.check_for_error(result)
            command = input()
        self.exhibit()


def main():
    plants_exhibition = Plants()
    n = int(input())
    plants_exhibition.initiate_plants(n)
    plants_exhibition.process_plants()


if __name__ == '__main__':
    main()
