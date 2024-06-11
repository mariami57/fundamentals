pirate_ship_status = list(map(int, input().split(">")))
war_ship_status = list(map(int, input().split(">")))
maximum_health_capacity = int(input())
command = input()
flag = False
while command != "Retire":
    if flag:
        break
    command = command.split()
    if command[0] == "Fire":
        index = int(command[1])
        if 0 <= index < len(war_ship_status):
            war_ship_status[index] -= int(command[2])
            if war_ship_status[index] <= 0:
                print("You won! The enemy ship has sunken.")
                flag = True
                break
    elif command[0] == "Defend":
        start_index = int(command[1])
        end_index = int(command[2])
        if 0 <= start_index < len(pirate_ship_status) and 0 <= end_index < len(pirate_ship_status):
            damaged_sections = pirate_ship_status[start_index:end_index+1]
            for current_section in range(len(damaged_sections)):
                damaged_sections[current_section] -= int(command[3])
                if damaged_sections[current_section] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    flag = True
                    break

            pirate_ship_status[start_index:end_index+1] = damaged_sections
    elif command[0] == "Repair":
        index = int(command[1])
        if 0 <= index < len(pirate_ship_status):
            pirate_ship_status[index] += int(command[2])
            if pirate_ship_status[index] > maximum_health_capacity:
                pirate_ship_status[index] = maximum_health_capacity
    elif command[0] == "Status":
        needs_repair = maximum_health_capacity * 0.2
        needs_repair_list = []
        for current_section in pirate_ship_status:
            if current_section < needs_repair:
                needs_repair_list.append(current_section)
        print(f"{len(needs_repair_list)} sections need repair.")

    command = input()

if not flag:
    print(f"Pirate ship status: {sum(pirate_ship_status)}")
    print(f"Warship status: {sum(war_ship_status)}")