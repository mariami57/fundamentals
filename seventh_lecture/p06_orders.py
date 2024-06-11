products = {}
total_cost = {}

input_line = input()

while input_line != "buy":
    input_line = input_line.split()
    name = input_line[0]
    price = float(input_line[1])
    current_quantity = int(input_line[2])

    if name not in products:
        quantity = current_quantity
        products[name] = [price, quantity]

    else:
        products[name][0] = price
        products[name][1] += current_quantity

    total_cost[name] = price * products[name][1]
    input_line = input()

for key in products.keys():
    print(f"{key} -> {(total_cost[key]):.2f}")

