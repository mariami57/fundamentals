n = int(input())
favourite_pieces = {}

for _ in range(n):
    input_line = input().split("|")
    piece, composer, key_note = input_line[0], input_line[1], input_line[2]
    favourite_pieces[piece] = [composer, key_note]

command = input()
while command != "Stop":
    command = command.split("|")
    action = command[0]
    piece_to_search = command[1]
    if action == "Add":
        if piece_to_search in favourite_pieces.keys():
            print(f"{piece_to_search} is already in the collection!")
        else:
            favourite_pieces[piece_to_search] = [command[2], command[3]]
            print(f"{piece_to_search} by {command[2]} in {command[3]} added to the collection!")
    elif action == "Remove":
        if piece_to_search in favourite_pieces.keys():
            print(f"Successfully removed {piece_to_search}!")
            favourite_pieces.pop(piece_to_search)
        else:
            print(f"Invalid operation! {piece_to_search} does not exist in the collection.")
    elif action == "ChangeKey":
        if piece_to_search in favourite_pieces.keys():
            favourite_pieces[piece_to_search][1] = command[2]
            print(f"Changed the key of {piece_to_search} to {command[2]}!")
        else:
            print(f"Invalid operation! {piece_to_search} does not exist in the collection.")

    command = input()

for pieces,values in favourite_pieces.items():
    print(f"{pieces} -> Composer: {values[0]}, Key: {values[1]}")
