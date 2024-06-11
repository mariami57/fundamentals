import re

list_of_names = input().split(", ")
names = []
distances = []
some_string = input()
while some_string != "end of race":
    distance_sum = 0
    name = re.findall(r"[A-Za-z]", some_string)
    current_name = ("".join(name))
    if current_name in list_of_names:
        distance = re.findall(r"\d", some_string)
        for digit in distance:
            distance_sum += int(digit)
        if current_name in names:
            index_of_distance = names.index(current_name)
            distances[index_of_distance] += distance_sum
        else:
            distances.append(int(distance_sum))
            names.append(current_name)
    some_string = input()

some_dict = {}

for i in range(len(names)):
    key = names[i]
    value = distances[i]
    some_dict[key] = value
sorted_dict = dict(sorted(some_dict.items(), key=lambda x:x[1], reverse=True))
top_racers = []
counter = 0
for k in sorted_dict.keys():
    if counter < 3:
        top_racers.append(k)
        counter += 1
print(f"1st place: {top_racers[0]}")
print(f"2nd place: {top_racers[1]}")
print(f"3rd place: {top_racers[2]}")

