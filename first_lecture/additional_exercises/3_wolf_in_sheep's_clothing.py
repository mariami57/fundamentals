animals = input()

animals_list = animals.split(", ")
last_element = animals_list[-1]
animals_reversed = animals_list[::-1]
sheep_position = 0
while True:
    for i in range(len(animals_reversed)):
        current_animal = animals_reversed[i]
        if current_animal == "sheep":
            sheep_position += 1
        elif current_animal == "wolf":
            break
    break

if last_element == "wolf":
    print("Please go away and stop eating my sheep")
elif last_element == "sheep":
    print(f"Oi! Sheep number {sheep_position}! You are about to be eaten by a wolf!")


