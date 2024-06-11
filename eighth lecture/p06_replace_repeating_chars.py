some_string = input()
last_added_char = ""
new_string = ""

for letter in some_string:
    if letter != last_added_char:
        last_added_char = letter
        new_string += letter

print(new_string)