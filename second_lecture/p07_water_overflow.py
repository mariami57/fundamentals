max_capacity = 255
filling_water = 0
n_lines = int(input())
for _ in range(n_lines):
    litres_of_water = int(input())
    if litres_of_water > max_capacity:
        print("Insufficient capacity!")
        continue
    max_capacity -= litres_of_water
    filling_water += litres_of_water

print(filling_water)