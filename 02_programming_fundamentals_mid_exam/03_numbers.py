some_string = input().split()
the_list = list(map(int, some_string))
sorted_list = sorted(the_list, reverse=True)
some_list = []
average = sum(the_list) / len(sorted_list)
counter = 0
for item in sorted_list:
    if counter == 5:
        break
    if item > average:
        some_list.append(item)
        counter += 1

if counter == 0:
    print("No")
else:
    print(" ".join(map(str, some_list)))
