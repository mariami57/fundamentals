some_string = input().split()

rounded_list = []
for num in some_string:
    rounded_list.append(round(float(num)))

print(rounded_list)