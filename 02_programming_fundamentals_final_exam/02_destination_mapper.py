import re

input_line = input()
travel_points = 0
destination_list = []
regex = r"([=\/])([A-Z][A-Za-z]{2,})\1"
matches = re.findall(regex, input_line)
for match in matches:
    destination = match[1]
    destination_list.append(destination)
    travel_points += len(destination)

print(f"Destinations: {', '.join(destination_list)}")
print(f"Travel Points: {travel_points}")

