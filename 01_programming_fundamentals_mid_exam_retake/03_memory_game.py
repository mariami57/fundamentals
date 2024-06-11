sequence_elements = input().split()
command = input()
n_moves = 0

while command != "end":
    if len(sequence_elements) == 0:
        break
    indices = command.split()
    index1 = int(indices[0])
    index2 = int(indices[1])
    n_moves += 1
    if index1 == index2 or (index1 not in range(len(sequence_elements)) or index2 not in range(len(sequence_elements))):
        middle = len(sequence_elements) // 2
        sequence_elements.insert(middle, f"-{n_moves}a")
        sequence_elements.insert(middle, f"-{n_moves}a")
        print("Invalid input! Adding additional elements to the board")
        command = input()
        continue
    elif sequence_elements[index1] == sequence_elements[index2]:
        element_to_remove = sequence_elements[index1]
        print(f"Congrats! You have found matching elements - {element_to_remove}!")
        for element in sequence_elements:
            if element_to_remove in sequence_elements:
                sequence_elements.remove(element_to_remove)
                if len(sequence_elements) == 1:
                    sequence_elements.clear()
            else:
                break
    else:
        print("Try again!")

    command = input()

if len(sequence_elements) > 0:
    print("Sorry you lose :(")
    print(" ".join(sequence_elements))
else:
    print(f"You have won in {n_moves} turns!")