input_line = input()
products = {}
while ":" in input_line:
    input_line = input_line.split(": ")
    key = input_line[0]
    value = input_line[1]

    if key in products:
        products[key] += int(value)
    else:
        products[key] = int(value)

    input_line = input()
total_quantity = 0
print("Products in stock:")
for product in products:
    print(f"- {product}: {products[product]}")
    total_quantity += products[product]

print(f"Total Products: {len(products)}")
print(f"Total Quantity: {total_quantity}")