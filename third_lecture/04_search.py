num = int(input())

magic_word = input()
all_strings = []
filtered_list = []
for _ in range(num):
    current_string = input()
    all_strings.append(current_string)

    if magic_word in current_string:
        filtered_list.append(current_string)

print(all_strings)
print(filtered_list)
