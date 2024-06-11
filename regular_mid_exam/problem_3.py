phones_list = input().split(", ")
command = input()

while command != "End":
    command = command.split(" - ")
    action = command[0]
    if action == "Add":
        phone_to_add = command[1]
        if phone_to_add not in phones_list:
            phones_list.append(phone_to_add)
    elif action == "Remove":
        phone_to_remove = command[1]
        if phone_to_remove in phones_list:
            phones_list.remove(phone_to_remove)
    elif action == "Bonus phone":
        phones = command[1].split(":")
        old_phone = phones[0]
        new_phone = phones[1]
        if old_phone in phones_list:
            new_phone_index = phones_list.index(old_phone) + 1
            phones_list.insert(new_phone_index,new_phone)
    elif action == "Last":
        last_phone = command[1]
        if last_phone in phones_list:
            phones_list.append(last_phone)
            phones_list.remove(last_phone)
    command = input()

print(", ".join(phones_list))