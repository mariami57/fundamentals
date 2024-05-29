budget = float(input())
flour_price = float(input())

eggs_price = 0.75 * flour_price
milk_price_per_litre = flour_price * 1.25
milk_price_per_quarter = milk_price_per_litre * 0.25
price_per_loaf = eggs_price + milk_price_per_quarter + flour_price
loaf_counter = 0
coloured_eggs_counter = 0
remaining_budget = 0
current_eggs_counter = 0
while budget > 0:
    remaining_budget = budget
    if remaining_budget - price_per_loaf <= 0 or current_eggs_counter < 0:
        break

    loaf_counter += 1
    budget -= price_per_loaf
    coloured_eggs_counter += 3
    lost_eggs = 0

    if loaf_counter % 3 == 0:
        lost_eggs = loaf_counter - 2
        coloured_eggs_counter -= lost_eggs

    current_eggs_counter = coloured_eggs_counter


print(f"You made {loaf_counter} loaves of Easter bread! Now you have {coloured_eggs_counter} eggs and {budget:.2f}BGN left.")

