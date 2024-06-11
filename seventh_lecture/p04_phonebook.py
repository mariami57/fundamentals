input_line = input()
phonebook = {}
while "-" in input_line:
    name, number = input_line.split("-")
    phonebook[name] = number
    input_line = input()


for _ in range(int(input_line)):
    searched_name = input()
    if searched_name in phonebook.keys():
        print(f"{searched_name} -> {phonebook[searched_name]}")
    else:
        print(f"Contact {searched_name} does not exist.")