elements = input().split()
products = {}

for i in range(0, len(elements),2):
    key = elements[i]
    value = elements[i+1]
    products[key] = int(value)

searched_products = input().split()
for product in searched_products:
    if product in products:
        print(f"We have {products[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")