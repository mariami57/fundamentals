some_string = input().split()
num = int(input())
some_list = []

for index in range(len(some_string)):
    current_num = int(some_string[index])
    some_list.append(current_num)
for _ in range(num):
    some_list.remove(min(some_list))

for x in some_list:
    if x == some_list[-1]:
        print(x)
    else:
        print(x, end=", ")




