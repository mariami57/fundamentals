n_cars = int(input())
cars = {}
for _ in range(n_cars):
    car, mileage, fuel = input().split("|")
    cars[car] = [mileage, fuel]
    cars[car][0] = int(mileage)
    cars[car][1] = int(fuel)

command = input()

while command != "Stop":
    command = command.split(" : ")
    action = command[0]
    current_car = command[1]
    if action == "Drive":
        distance = int(command[2])
        current_fuel = int(command[3])
        if cars[current_car][1] >= current_fuel:
            cars[current_car][1] -= current_fuel
            cars[current_car][0] += distance
            print(f"{current_car} driven for {distance} kilometers. {current_fuel} liters of fuel consumed.")
        else:
            print("Not enough fuel to make that ride")
        if cars[current_car][0] >= 100000:
            print(f"Time to sell the {current_car}!")
    elif action == "Refuel":
        fuel_to_refill = int(command[2])
        if cars[current_car][1] < 75 and (cars[current_car][1] + fuel_to_refill > 75):
            diff = 75 - cars[current_car][1]
            cars[current_car][1] += diff
            print(f"{current_car} refueled with {diff} liters")
        else:
            cars[current_car][1] += fuel_to_refill
            print(f"{current_car} refueled with {fuel_to_refill} liters")
    elif action == "Revert":
        kilometers = int(command[2])
        cars[current_car][0] -= kilometers
        if cars[current_car][0] < 10000:
            cars[current_car][0] = 10000
        else:
            print(f"{current_car} mileage decreased by {kilometers} kilometers")
    command = input()
for car, values in cars.items():
    if cars[car][0] >= 100000:
        continue
    else:
        print(f"{car} -> Mileage: {cars[car][0]} kms, Fuel in the tank: {cars[car][1]} lt.")



