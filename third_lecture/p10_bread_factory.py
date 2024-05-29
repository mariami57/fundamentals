initial_energy = 100
initial_coins = 100
event_sting = input().split("|")
flag = False

for event in event_sting:
    current_event = event.split("-")
    event_type = current_event[0]
    event_value = int(current_event[1])
    if event_type == "rest":
        current_energy = initial_energy
        initial_energy += event_value
        if initial_energy > 100:
            initial_energy = 100
        gained_energy = initial_energy - current_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {initial_energy}.")

    elif event_type == "order":
        if initial_energy >= 30:

            initial_coins += event_value
            initial_energy -= 30
            print(f"You earned {event_value} coins.")
        else:
            initial_energy += 50
            print("You had to rest!")
            continue

    else:
        if initial_coins >= event_value:

            initial_coins -= event_value
            print(f"You bought {event_type}.")
        else:
            flag = True
            break

if flag:
    print(f"Closed! Cannot afford {event_type}.")

else:
    print("Day completed!")
    print(f"Coins: {initial_coins}")
    print(f"Energy: {initial_energy}")