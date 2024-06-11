sequence_strings = input().split()
new_string = []
for string in sequence_strings:
    updated_string = string * len(string)
    new_string.append(updated_string)

print("".join(new_string))