number_of_wagons = int(input())
wagons = [0] * number_of_wagons

while True:
    command = input().split()

    if command[0] == "End":
        print(wagons)
        break
    elif command[0] == "add":
        people = int(command[1])
        wagons[-1] += people
    elif command[0] == "insert":
        index = int(command[1])
        people = int(command[2])
        wagons[index] += people
    elif command[0] == "leave":
        index = int(command[1])
        people = int(command[2])
        wagons[index] -= people





