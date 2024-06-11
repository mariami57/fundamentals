message = input()

command = input()
error_flag = False
while command != "Reveal":
    command = command.split(":|:")
    action = command[0]
    if action == "InsertSpace":
        index = int(command[1])
        left_part = message[:index]
        right_part = message[index:]
        message = left_part + " " + right_part
    elif action == "Reverse":
        substring = command[1]
        if substring in message:
            substring_index = message.find(substring)
            message = message[:substring_index] + message[substring_index + len(substring):]
            substring = substring[::-1]
            message += substring
        else:
            error_flag = True
    elif action == "ChangeAll":
        substring = command[1]
        replacement = command[2]
        message = message.replace(substring, replacement)
    if error_flag:
        print("error")
        error_flag = False
    else:
        print(message)
    command = input()

print(f"You have a new text message: {message}")