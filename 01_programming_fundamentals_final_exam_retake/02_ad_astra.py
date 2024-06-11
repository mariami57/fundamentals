import re

input_line = input()
total_calories = 0
regex = r"([#\|])([A-Za-z\s]+)\1(\d{2}\/\d{2}\/\d{2})\1([0-9]{1,5})\1"
matches = re.findall(regex, input_line)


for match in matches:
    food, expiration_date, calories = match[1], match[2], match[3]
    total_calories += int(calories)

n_days = total_calories // 2000
print(f"You have food to last you for: {n_days} days!")

for match in matches:
    print(f"Item: {match[1]}, Best before: {match[2]}, Nutrition: {match[3]}")
