class Zoo:
    __animals = 0

    def __init__(self, name):
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

    def get_info(self, species):
        some_string = ""
        if specific_species == "mammal":
            some_string += f"Mammals in {zoo_name}: {', '.join(self.mammals)}"
        elif specific_species == "fish":
            some_string += f"Fishes in {zoo_name}: {', '.join(self.fishes)}"
        elif specific_species == "bird":
            some_string += f"Birds in {zoo_name}: {', '.join(self.birds)}"
        some_string += f"\nTotal animals: {Zoo.__animals}"

        return some_string


zoo_name = input()
zoo_object = Zoo(zoo_name)
n = int(input())
for number in range(n):
    species, name = input().split()
    zoo_object.add_animal(species, name)

specific_species = input()

print(zoo_object.get_info(specific_species))


