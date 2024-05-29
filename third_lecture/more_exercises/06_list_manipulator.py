import sys

numbers_list = input().split()
command = input()


while command != "end":
    command = command.split()
    action = command[0]
    if action == "exchange":
        index = int(command[1])
        if 0 <= index < len(numbers_list):
            first_list = numbers_list[:index+1]
            second_list = numbers_list[index+1:]
            numbers_list = second_list + first_list
        else:
            print("Invalid index")

    command = input()

print(f"[{', '.join(numbers_list)}]")