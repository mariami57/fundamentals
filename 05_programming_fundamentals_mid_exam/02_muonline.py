rooms = input().split("|")
health = 100
bitcoins = 0
best_room = 0
killed = False
for room in rooms:
    room = room.split()
    command = room[0]
    number = int(room[1])
    best_room +=1
    if command == "potion":
        if health + number > 100:
            number = 100 - health
        health += number
        print(f"You healed for {number} hp.")
        print(f"Current health: {health} hp.")
    elif command == "chest":
        bitcoins += number
        print(f"You found {number} bitcoins.")
    else:
        health -= number
        if health > 0:
            print(f"You slayed {command}.")
        else:
            killed = True
            print(f"You died! Killed by {command}.")
            print(f"Best room: {best_room}")
            break


if not killed:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")
