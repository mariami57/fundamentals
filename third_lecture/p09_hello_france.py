items = input().split("|")
budget = float(input())
profit = 0
profit_per_item = 0
profit_all_items = 0
for item in items:
    item_price = item.split("->")
    if budget < float(item_price[1]):
        continue
    if ("Clothes" in item_price and float(item_price[1]) <= 50) or \
        ("Shoes" in item_price and float(item_price[1]) <= 35) or \
            ("Accessories" in item_price and float(item_price[1]) <= 20.5):
        budget -= float(item_price[1])
        profit_per_item = 1.4 * float(item_price[1])
        profit_all_items += profit_per_item
        profit = profit - float(item_price[1]) + profit_per_item
        print(f"{profit_per_item:.2f}", end=" ")
    if budget == 0:
        break
print()
print(f"Profit: {profit:.2f}")
total_profit = profit_all_items + budget
if total_profit >= 150:
    print("Hello, France!")

else:
    print("Not enough money.")


