some_array = input().split()
command = input().split()

while command[0] != "end":
    if command[0] == "swap":
        index1 = int(command[1])
        index2 = int(command[2])
        some_array[index1],some_array[index2] = some_array[index2], some_array[index1]
    elif command[0] == "multiply":
        index1 = int(command[1])
        index2 = int(command[2])
        some_array[index1] = str(int(some_array[index1]) * int(some_array[index2]))
    elif command[0] == "decrease":
        for index in range(len(some_array)):
            some_array[index] = str(int(some_array[index]) - 1)

    command = input().split()

print(", ".join(some_array))
