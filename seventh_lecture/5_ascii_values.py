input_line = input().split(", ")

# some_dict = {char: ord(char) for char in input_line}
some_dict = {}

for char in input_line:
    key = char
    some_dict[key] = ord(char)

print(some_dict)