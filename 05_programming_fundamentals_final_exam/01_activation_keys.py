raw_key = input()
command = input()

while command != "Generate":
    command = command.split(">>>")
    action = command[0]
    if action == "Contains":
        substring = command[1]
        if substring in raw_key:
            print(f"{raw_key} contains {substring}")
        else:
            print("Substring not found!")
    elif action == "Flip":
        case = command[1]
        start_index, end_index = int(command[2]), int(command[3])
        part_of_string = raw_key[start_index:end_index]
        left_part = raw_key[:start_index]
        right_part = raw_key[end_index:]
        if case.lower() == "lower":
            part_of_string = part_of_string.lower()
        elif case.lower() == "upper":
            part_of_string = part_of_string.upper()
        raw_key = left_part + part_of_string + right_part
        print(raw_key)
    elif action == "Slice":
        start_index, end_index = int(command[1]), int(command[2])
        part_of_string = raw_key[start_index:end_index]
        left_part = raw_key[:start_index]
        right_part = raw_key[end_index:]
        raw_key = left_part + right_part
        print(raw_key)
    command = input()

print(f"Your activation key is: {raw_key}")

