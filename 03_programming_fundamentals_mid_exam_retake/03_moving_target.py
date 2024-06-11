targets = [int(x) for x in input().split()]
command = input().split()

while command[0] != "End":
    index = int(command[1])
    value = int(command[2])
    if command[0] == "Shoot":
        if 0 <= index < len(targets):
            targets[index] -= value
            if targets[index] <= 0:
                targets.pop(index)
    elif command[0] == "Add":
        if 0 <= index < len(targets):
            targets.insert(index, value)
        else:
            print("Invalid placement!")
    elif command[0] == "Strike":
        radius_up = index + value + 1
        radius_down = index - value
        if 0 <= radius_down < radius_up < len(targets):
            del targets[radius_down:radius_up]

        else:
            print("Strike missed!")
    command = input().split()

print("|".join(str(x) for x in targets))