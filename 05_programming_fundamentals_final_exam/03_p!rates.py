command = input()
cities = {}
while command != "Sail":
    city, population, gold = command.split("||")
    if city not in cities:
        cities[city] = [int(population), int(gold)]
    else:
        cities[city][0] += int(population)
        cities[city][1] += int(gold)
    command = input()
second_command = input()
while second_command != "End":
    second_command = second_command.split("=>")
    action = second_command[0]
    town = second_command[1]
    if action == "Plunder":
        people = int(second_command[2])
        current_gold = int(second_command[3])
        cities[town][0] -= people
        cities[town][1] -= current_gold
        print(f"{town} plundered! {current_gold} gold stolen, {people} citizens killed.")
        if cities[town][0] <= 0 or cities[town][1] <= 0:
            del cities[town]
            print(f"{town} has been wiped off the map!")
    elif action == "Prosper":
        amount_of_gold = int(second_command[2])
        if amount_of_gold < 0:
            print("Gold added cannot be a negative number!")
        else:
            cities[town][1] += amount_of_gold
            print(f"{amount_of_gold} gold added to the city treasury. {town} now has {cities[town][1]} gold.")
    second_command = input()

if len(cities) > 0:
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
    for key in cities.keys():
        print(f"{key} -> Population: {cities[key][0]} citizens, Gold: {cities[key][1]} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")






