password = input()
command = input()

while command != "Done":
    command = command.split()
    action = command[0]
    if action == "TakeOdd":
        new_password = ""
        for index in range(1, len(password), 2):
            new_password += password[index]
        password = new_password
        print(password)
    elif action == "Cut":
        index = int(command[1])
        end = int(command[2])
        password = password[:index] + password[index+end:]
        print(password)
    elif action == "Substitute":
        substring = command[1]
        substitute = command[2]
        if substring in password:
            password = password.replace(substring, substitute)
            print(password)
        else:
            print("Nothing to replace!")
    command = input()

print(f"Your password is: {password}")


