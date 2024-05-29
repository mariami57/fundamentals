n_orders = int(input())
total_price = 0
for _ in range(n_orders):
    price_per_capsule = float(input())
    n_days = int(input())
    capsules_per_day = int(input())

    if 0.01 <= price_per_capsule <= 100 and 1 <= n_days <= 31 and 1 <= capsules_per_day <= 2000:
        order_price = price_per_capsule * n_days * capsules_per_day
        print(f"The price for the coffee is: ${order_price:.2f}")

    else:
        continue
    total_price += order_price

print(f"Total: ${total_price:.2f}")
