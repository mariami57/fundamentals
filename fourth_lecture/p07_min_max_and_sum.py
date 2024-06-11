def min_number(the_list):
    return min(the_list), max(the_list), sum(the_list)


some_string = input().split()
some_list = []
for num in some_string:
    some_list.append(int(num))

min_list, max_list, sum_list = min_number(some_list)

print(f"The minimum number is {min_list}")
print(f"The maximum number is {max_list}")
print(f"The sum number is: {sum_list}")