shopping_list = input().split("!")
command = input()

while command != "Go Shopping!":
    command = command.split()
    action = command[0]
    item = command[1]

    if action == "Urgent":
        if item not in shopping_list:
            shopping_list.insert(0,item)
    elif action == "Unnecessary":
        if item in shopping_list:
            shopping_list.remove(item)
    elif action == "Correct":
        if item in shopping_list:
            index = shopping_list.index(item)
            item_to_add = command[2]
            shopping_list.insert(index, item_to_add)
            shopping_list.remove(item)
    elif action == "Rearrange":
        if item in shopping_list:
            shopping_list.remove(item)
            shopping_list.append(item)
    command = input()

print(", ".join(shopping_list))



