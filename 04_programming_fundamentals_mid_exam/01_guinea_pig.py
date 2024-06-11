food, hay, cover, weight = float(input()), float(input()), float(input()), float(input())
food_in_grams = food * 1000
enough = True
for day in range(1, 31):
    food_in_grams -= 300
    if day % 2 == 0:
        hay -= (food_in_grams / 1000) * 0.05
    if day % 3 == 0:
        cover -= weight / 3

    if food_in_grams <= 0 or hay <= 0 or cover <= 0:
        print("Merry must go to the pet store!")
        enough = False
        break


if enough:
    print(f"Everything is fine! Puppy is happy! Food: {food_in_grams / 1000:.2f}, Hay: {hay:.2f}, Cover: {cover:.2f}.")

