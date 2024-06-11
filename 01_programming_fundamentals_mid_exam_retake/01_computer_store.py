command = input()
flag = False
price_without_taxes = 0
while command != "special" and command != "regular":
    command_float = float(command)
    if command_float < 0:
        print("Invalid price!")
        command = input()
        continue
    price_without_taxes += command_float
    command = input()
taxes = price_without_taxes * 0.2
total_price_with_taxes = price_without_taxes + taxes
if total_price_with_taxes == 0:
    flag = True
if command == "special":
    total_price_with_taxes *= 0.9
if flag:
    print("Invalid order!")
else:
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {price_without_taxes:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    print(f"Total price: {total_price_with_taxes:.2f}$")

