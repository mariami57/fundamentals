stops = input()
command = input()

while command != "Travel":
    command = command.split(":")
    action = command[0]
    if action == "Add Stop":
        index = int(command[1])
        string_to_insert = command[2]
        if 0 <= index < len(stops):
            first_part = stops[:index]
            second_part = stops[index:]
            stops = first_part + string_to_insert + second_part
    elif action == "Remove Stop":
        start_index, end_index = int(command[1]), int(command[2])
        if 0 <= start_index < len(stops) and 0 <= end_index < len(stops):
            stops = stops[:start_index] + stops[end_index+1:]
    elif action == "Switch":
        old_string, new_string = command[1], command[2]
        if old_string in stops:
            stops = stops.replace(old_string,new_string)
    print(stops)
    command = input()

print(f"Ready for world tour! Planned stops: {stops}")