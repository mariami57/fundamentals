initial_energy = int(input())
command = input()
won_battles = 0
while command != "End of battle":
    distance = int(command)
    if initial_energy < distance:
        print(f"Not enough energy! Game ends with {won_battles} won battles and {initial_energy} energy")
        break
    else:
        won_battles += 1
        initial_energy -= distance
    if won_battles % 3 == 0:
        initial_energy += won_battles
    command = input()


if command == "End of battle":
    print(f"Won battles: {won_battles}. Energy left: {initial_energy}")