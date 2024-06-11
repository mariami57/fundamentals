first_line_strings = input().split(", ")
second_line_strings = input().split(", ")
list_of_strings = []
for index in range(len(first_line_strings)):
    for second_index in range(len(second_line_strings)):
        if first_line_strings[index] in second_line_strings[second_index]:
            if first_line_strings[index] in list_of_strings:
                continue
            else:
                list_of_strings.append(first_line_strings[index])

print(list_of_strings)