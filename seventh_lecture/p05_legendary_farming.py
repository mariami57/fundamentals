key_elements = {"shards": 0, "fragments": 0, "motes": 0}
flag = False
while True:
    input_line = input().split()
    for index in range(0, len(input_line), 2):
        quantity = int(input_line[index])
        material = input_line[index + 1].lower()
        if material not in key_elements.keys():
            key_elements[material] = 0

        key_elements[material] += quantity
        if key_elements["shards"] >= 250:
            key_elements["shards"] -= 250
            print("Shadowmourne obtained!")
            flag = True
            break
        elif key_elements["fragments"] >= 250:
            key_elements["fragments"] -= 250
            print("Valanyr obtained!")
            flag = True
            break
        elif key_elements["motes"] >= 250:
            key_elements["motes"] -= 250
            print("Dragonwrath obtained!")
            flag = True
            break
    if flag:
        break

for material, quantity in key_elements.items():
    print(f"{material}: {quantity}")
