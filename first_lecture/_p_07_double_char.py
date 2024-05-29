current_string = input()

while current_string != "End":
    new_string = ""
    if current_string == "SoftUni":
        current_string = input()
        continue
    for character in current_string:
        new_string += character * 2
    print(new_string)
    current_string = input()


