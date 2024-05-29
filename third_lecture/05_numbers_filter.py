n = int(input())

number_list = []
for _ in range(n):
    number = int(input())
    number_list.append(number)

word = input()
list_for_print = []

for element in number_list:
    if element % 2 == 0 and word == "even":
        list_for_print.append(element)
    elif element % 2 != 0 and word == "odd":
        list_for_print.append(element)
    elif element >= 0 and word == "positive":
        list_for_print.append(element)
    elif element < 0 and word == "negative":
        list_for_print.append(element)

print(list_for_print)
