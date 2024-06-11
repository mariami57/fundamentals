n = int(input())
heroes = {}
for _ in range(n):
    name, hit_points, mana_points = input().split()
    heroes[name] = [int(hit_points), int(mana_points)]

command = input()

while command != "End":
    command = command.split(" - ")
    action = command[0]
    current_name = command[1]
    if action == "CastSpell":
        mp_needed, spell_name = int(command[2]), command[3]
        if heroes[current_name][1] >= mp_needed:
            heroes[current_name][1] -= mp_needed
            print(f"{current_name} has successfully cast {spell_name} and now has {heroes[current_name][1]} MP!")
        else:
            print(f"{current_name} does not have enough MP to cast {spell_name}!")
    elif action == "TakeDamage":
        damage, attacker = int(command[2]), command[3]
        heroes[current_name][0] -= damage
        if heroes[current_name][0] > 0:
            print(f"{current_name} was hit for {damage} HP by {attacker} and now has {heroes[current_name][0]} HP left!")
        else:
            print(f"{current_name} has been killed by {attacker}!")
    elif action == "Recharge":
        amount = int(command[2])
        amount_to_recharge = 200 - heroes[current_name][1]
        heroes[current_name][1] += amount
        if heroes[current_name][1] > 200:
            heroes[current_name][1] = 200
            amount_to_print = amount_to_recharge
        else:
            amount_to_print = amount
        print(f"{current_name} recharged for {amount_to_print} MP!")
    elif action == "Heal":
        amount_to_heal = int(command[2])
        amount_left = 100 - heroes[current_name][0]
        heroes[current_name][0] += amount_to_heal
        if heroes[current_name][0] > 100:
            heroes[current_name][0] = 100
            amount_to_print_heal = amount_left
        else:
            amount_to_print_heal = amount_to_heal
        print(f"{current_name} healed for {amount_to_print_heal} HP!")

    command = input()

for keys in heroes.keys():
    if heroes[keys][0] <= 0:
        continue
    else:
        print(keys)
        print(f"HP: {heroes[keys][0]}")
        print(f"MP: {heroes[keys][1]}")


