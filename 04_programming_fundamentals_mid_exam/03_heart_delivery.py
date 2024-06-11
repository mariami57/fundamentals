even_integers = [int(x) for x in input().split("@")]

command = input()
for i in range(len(even_integers)):
    while command != "Love!":
        command = command.split()
        action = command[0]
        jump_length = int(command[1])
        first_jump = i + jump_length

        if first_jump > len(even_integers) - 1:
            first_jump = 0
        if even_integers[first_jump] == 0:
            print(f"Place {first_jump} already had Valentine's day.")
        else:
            even_integers[first_jump] -= 2
            if even_integers[first_jump] == 0:
                print(f"Place {first_jump} has Valentine's day." )

        command = input()
        i = first_jump


print(f"Cupid's last position was {first_jump}.")

if sum(even_integers) == 0:
    print("Mission was successful.")
else:
    mission_failed = len([house for house in even_integers if house > 0])
    print(f"Cupid has failed {mission_failed} places.")


