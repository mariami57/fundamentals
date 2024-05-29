number_list = []
for _ in range(4):
    number = int(input())
    number_list.append(number)

total = ((number_list[0] + number_list[1]) // number_list[2]) * number_list[3]

print(total)
