initial_loot = input().split("|")
command = input()
while command != "Yohoho!":
    command = command.split()
    action = command[0]
    if action == "Loot":
        for index in range(1, len(command)):
            item = command[index]
            if item not in initial_loot:
                initial_loot.insert(0, item)
    elif action == "Drop":
        index = int(command[1])
        if 0 <= index < len(initial_loot):
            initial_loot.append(initial_loot[index])
            initial_loot.pop(index)
    elif action == "Steal":
        last_count = int(command[1])
        removed_items = 0
        removed_list = []
        for index2 in range((len(initial_loot) -1), -1, -1):
            item = initial_loot[index2]
            if removed_items < last_count:
                removed_list.append(item)
                initial_loot.remove(item)
                removed_items += 1
        rem_reversed_list = removed_list[::-1]
        print(", ".join(rem_reversed_list))
    command = input()


if len(initial_loot) != 0:
    total_length = 0
    for item in initial_loot:
        total_length += len(item)

    average_treasure_gain = total_length / len(initial_loot)
    print(f"Average treasure gain: {average_treasure_gain:.2f} pirate credits.")
else:
    print("Failed treasure hunt.")
