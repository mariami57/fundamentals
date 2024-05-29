level_of_fire = input().split("#")
water_amount = int(input())
effort = 0
total_fire = 0

print("Cells:")
for cell in level_of_fire:
    cell_split = cell.split(" = ")
    if water_amount < int(cell_split[1]):
        continue
    if ("High" in cell and 81 <= int(cell_split[1]) <= 125) or\
            ("Medium" in cell and 51 <= int(cell_split[1]) <= 80) or \
            ("Low" in cell and 1 <= int(cell_split[1]) <= 50):
        water_amount -= int(cell_split[1])
        total_fire += int(cell_split[1])
        effort += 0.25 * int(cell_split[1])
        print("-",int(cell_split[1]))
    if water_amount == 0:
        break

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
