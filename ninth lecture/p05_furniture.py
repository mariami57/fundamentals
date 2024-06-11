import re
bought = []
input_line = input()
regex = r">>([A-Za-z]+)<<(\d+[\.\d]+)!(\d+)"
total_cost = 0
while input_line != "Purchase":
    matches = re.search(regex, input_line)
    if matches:
        furniture, price, quantity = matches.groups()
        bought.append(furniture)
        total_cost += float(price) * int(quantity)

    input_line = input()

print("Bought furniture:")
for item in bought:
    print(item)

print(f"Total money spend: {total_cost:.2f}")