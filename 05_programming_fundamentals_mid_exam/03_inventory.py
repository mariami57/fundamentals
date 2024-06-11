journal = input().split(", ")
command = input()

while command != "Craft!":
    command = command.split(" - ")
    action = command[0]
    item = command[1]
    if action == "Collect":
        if item not in journal:
            journal.append(item)
    elif action == "Drop":
        if item in journal:
            journal.remove(item)
    elif action == "Combine Items":
        item = item.split(":")
        current_item = item[0]
        new_item = item[1]
        if current_item in journal:
            item_index = journal.index(current_item)
            journal.insert(item_index + 1, new_item)
    elif action == "Renew":
        if item in journal:
            journal.remove(item)
            journal.append(item)
    command = input()

print(", ".join(journal))
