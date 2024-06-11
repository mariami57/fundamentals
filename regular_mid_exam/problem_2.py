coffees_list = input().split()
n_commands = int(input())

for _ in range(n_commands):
    current_command = input().split()
    action = current_command[0]
    if action == "Include":
        coffees_list.append(current_command[1])
    elif action == "Remove":
        n_coffees = int(current_command[2])
        if 0 < n_coffees <= len(coffees_list):
            if current_command[1] == "first":
                counter_removed_coffees = 0
                while counter_removed_coffees < n_coffees:
                    coffees_list.remove(coffees_list[0])
                    counter_removed_coffees += 1
            elif current_command[1] == "last":
                counter_removed_coffees = 0
                while counter_removed_coffees < n_coffees:
                    coffees_list.remove(coffees_list[-1])
                    counter_removed_coffees += 1
    elif action == "Prefer":
        first_index = int(current_command[1])
        second_index = int(current_command[2])
        if 0 <= first_index < len(coffees_list) and 0 <= second_index < len(coffees_list):
            coffees_list[first_index], coffees_list[second_index] = coffees_list[second_index], coffees_list[first_index]
    else:
        coffees_list.reverse()

print(f"Coffees:\n{' '.join(coffees_list)}")



