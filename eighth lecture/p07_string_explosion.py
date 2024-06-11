some_string = input()

explosion_strength = 0
final_string = ""
for index in range(len(some_string)):
    if explosion_strength > 0 and some_string[index] != ">":
        explosion_strength -= 1
    elif some_string[index] == ">":
        explosion_strength += int(some_string[index+1])
        final_string += some_string[index]
    else:
        final_string += some_string[index]

print(final_string)