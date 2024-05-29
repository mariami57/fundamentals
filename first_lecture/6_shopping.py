budget = int(input())
input_line = input()

while input_line != "End":
    price = int(input_line)
    if budget < price:
        print("You went in overdraft!" )
        break
    budget -= price

    input_line = input()
else:
    print("You bought everything needed.")