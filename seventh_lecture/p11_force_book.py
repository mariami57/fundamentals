input_line = input()
forces = {}
part_of_the_force = False
while input_line != "Lumpawaroo":
    if " | " in input_line:
        force_side, user = input_line.split(" | ")
        for value in forces.values():
            if user in value:
                part_of_the_force = True
                break
        if not part_of_the_force:
            if force_side not in forces.keys():
                forces[force_side] = [user]
            elif force_side in forces.keys():
                forces[force_side].append(user)
        else:
            break

    elif " -> " in input_line:
        user, force_side = input_line.split(" -> ")
        for value in forces.values():
            if user in value:
                value.remove(user)
                break
        if force_side not in forces.keys():
            forces[force_side] = []
        forces[force_side].append(user)
        print(f"{user} joins the {force_side} side!")
    input_line = input()


for key, values in forces.items():
    if len(values) > 0:
        print(f"Side: {key}, Members: {len(values)}")
        for value in forces[key]:
            print(f"! {value}")
