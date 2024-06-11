some_string = input()

some_dict = {}

for char in range(len(some_string)):
    if some_string[char] == " ":
        continue
    key = some_string[char]
    if key in some_dict:
        some_dict[key] += 1
    else:
        some_dict[key] = 1

for key, value in some_dict.items():
    print(f"{key} -> {value}")