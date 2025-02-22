class Zoo:
    __animals = 0

    def __init__(self, name: str):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)
        Zoo.__animals += 1

    def get_info(self, species: str):
        if species == "mammal":
            result = str(f"Mammals in {self.name}: {', '.join(self.mammals)}")
        elif species == "fish":
            result = str(f"Fishes in {self.name}: {', '.join(self.fishes)}")
        elif species == "bird":
            result = str(f"Birds in {self.name}: {', '.join(self.birds)}")

        return f"{result}\nTotal animals: {Zoo.__animals}"


zoo_name = input()
zoo = Zoo(zoo_name)
animals = int(input())
for i in range(animals):
    specie, name = input().split()
    zoo.add_animal(specie, name)
species = input()
print(zoo.get_info(species))
