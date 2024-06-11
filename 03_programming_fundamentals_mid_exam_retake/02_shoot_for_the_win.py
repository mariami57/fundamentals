targets = [int(x) for x in input().split()]
command = input()
counter = 0
while command != "End":
    index = int(command)

    if 0 <= index < len(targets):
        target = targets[index]
        targets[index] = -1
        counter += 1
        for target_index in range(len(targets)):
            if targets[target_index] == -1:
                continue
            if targets[target_index] <= target:
                targets[target_index] += target
            else:
                targets[target_index] -= target

    command = input()

print(f"Shot targets: {counter} -> {' '.join(str(x) for x in targets)}")