some_string = input().split()
some_list = []
for num in some_string:
    some_list.append(int(num))

some_list.sort(key=lambda x: x)

print(some_list)