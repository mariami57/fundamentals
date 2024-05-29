some_string = input()
some_list = some_string.split("")
opposite_list = []
for element in some_list:
    if int(element) > 0:
        opposite_list.append(-int(element))
    elif int(element) < 0:
        opposite_list.append(abs(int(element)))
    elif int(element) == 0:
        opposite_list.append(int(element))

print(opposite_list)

