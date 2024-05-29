string = input()
letter_list = list(string)
upper_list = []
counter = 0
for i in string:
    if i.isupper():
        upper_list.append(counter)
    counter += 1
print(upper_list)