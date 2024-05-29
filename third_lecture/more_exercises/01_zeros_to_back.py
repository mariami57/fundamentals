some_string = list(map(int,input().split(", ")))
sorted_string = []
zero_list = []


for element in some_string:
    if element == 0:
        zero_list.append(element)
    else:
        sorted_string.append(element)

final_list = sorted_string + zero_list

print(final_list)