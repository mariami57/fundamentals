some_string = input().split()
abs_list = []
for num in some_string:
    abs_list.append(abs(float(num)))

print(abs_list)