quantity = int(input())
days_left = int(input())

ornament_set_price = 2
tree_skirt_price = 5
tree_garland_price = 3
tree_lights_price = 15
spirit_points_counter = 0
total_cost = 0

for current_day in range(1, days_left+1):
    if current_day % 11 == 0:
        quantity += 2
    if current_day % 2 == 0:
        spirit_points_counter += 5
        total_cost += ornament_set_price * quantity
    if current_day % 3 == 0:
        spirit_points_counter += 13
        total_cost += (tree_garland_price + tree_skirt_price) * quantity
    if current_day % 5 == 0:
        spirit_points_counter += 17
        total_cost += tree_lights_price * quantity
        if current_day % 3 == 0:
            spirit_points_counter += 30
    if current_day % 10 == 0:
        spirit_points_counter -= 20
        total_cost += tree_skirt_price + tree_garland_price + tree_lights_price


if days_left % 10 == 0:
    spirit_points_counter -= 30

print(f"Total cost: {total_cost}")
print(f"Total spirit: {spirit_points_counter}")

