input_line = input()
metals = {}
while input_line != "stop":
    metal = input_line
    quantity = int(input())
    if metal not in metals.keys():
        metals[metal] = quantity

    metals[metal] += quantity

    input_line = input()

for metal, quantity in metals.items():
    print(f"{metal} -> {quantity}")

