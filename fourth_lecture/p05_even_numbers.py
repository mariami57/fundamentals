some_string = input().split()
list_int = []
for num in some_string:
    list_int.append(int(num))

is_even = lambda x: x % 2 == 0
filtered_numbers = list(filter(is_even, list_int))
print(filtered_numbers)