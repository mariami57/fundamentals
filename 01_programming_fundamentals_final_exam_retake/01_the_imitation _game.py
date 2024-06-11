message = input()
command = input()

while command != "Decode":
    command = command.split("|")
    action = command[0]
    if action == "ChangeAll":
        substring = command[1]
        replacement = command[2]
        message = message.replace(substring, replacement)
    elif action == "Insert":
        index = int(command[1])
        value = command[2]
        message = message[:index] + value + message[index:]
    elif action == "Move":
        n_letters = int(command[1])
        letters_to_remove = message[:n_letters]
        letters_left = message[n_letters:]
        message = letters_left + letters_to_remove
    command = input()

print(f"The decrypted message is: {message}")