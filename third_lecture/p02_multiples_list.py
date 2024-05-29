factor = int(input())
count = int(input())
number_list = []
for number in range(1,count+1):
    multiple = number * factor
    number_list.append(multiple)

print(number_list)