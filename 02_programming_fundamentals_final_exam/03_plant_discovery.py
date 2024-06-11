n = int(input())
plants = {}

for _ in range(n):
    current_plant, rarity = input().split("<->")
    plants[current_plant] = plants.get(current_plant, {})
    plants[current_plant]["rarity"] = int(rarity)
    plants[current_plant]["rating"] = []

command = input()

while command != "Exhibition":
    command = command.split(": ")
    action = command[0]
    rest = command[1].split(" - ")
    plant = rest[0]
    if plant in plants:
        if action == "Rate":
            rating = float(rest[1])
            plants[plant]["rating"].append(rating)
        elif action == "Update":
            new_rarity = rest[1]
            plants[plant]["rarity"] = new_rarity
        elif action == "Reset":
            plants[plant]["rating"] = []
    else:
        print("error")
    command = input()
print("Plants for the exhibition:")

for plant in plants:
    if sum(plants[plant]["rating"]) != 0:
        average = sum(plants[plant]["rating"]) / len(plants[plant]["rating"])
    else:
        average = 0
    print(f"- {plant}; Rarity: {plants[plant]['rarity']}; Rating: {average:.2f}")
