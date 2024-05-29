gifts_string = input().split()
command = input()
gifts_list = []

while command != "No Money":
    command = command.split()

    if command[0] == "OutOfStock":
        gift_to_remove = command[1]
        while gift_to_remove in gifts_string:
            index = gifts_string.index(gift_to_remove)
            gifts_string[index] = "None"

    elif command[0] == "Required":
        gift_to_replace = command[1]
        index = int(command[2])
        if len(gifts_string) > index >= 0:
            gifts_string[index] = gift_to_replace

    elif command[0] == "JustInCase":
        gifts_string[-1] = command[1]

    command = input()

for element in gifts_string:
    if element == "None":
        continue
    else:
        print(element, end=" ")


